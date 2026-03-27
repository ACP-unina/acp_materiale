from concurrent import futures
import time
import uuid
import sys

import grpc
import order_management_pb2_grpc
import order_management_pb2

from pymongo import MongoClient

import logging

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer): 

    def __init__(self, orders_collection, shipment_collection):
        
        # orderDict lo utilizziamo per mantenere la lista degli ordini fatti
        # E.g.: 
        """ Un Order è del tipo
        {'3632b44c-0c94-11ef-bf4b-acde48001122': 
                id: "3632b44c-0c94-11ef-bf4b-acde48001122"
                items: "Item - A"
                items: "Item - B"
                items: "Item - C"
                description: "This is a Sample order - 1 : description."
                price: 2450.5
                destination: "San Jose, CA"
        }
        """
        
        self.orders_collection = orders_collection
        self.shipment_collection = shipment_collection


    # Unary RPC
    def getOrder(self, request, context):
        
        order_db_find = self.orders_collection.find_one({"id" : request.value})
                
        ## costruisco il Order da mandare usando il dict ritornato da mongodb
        order_to_return = order_management_pb2.Order(id=order_db_find['id'],
                                                        items=order_db_find['items'],
                                                        description=order_db_find['description'],
                                                        price=order_db_find['price'],
                                                        destination=order_db_find['destination'])

        if order_to_return is not None: 
            logging.debug('[OrderManagementServicer] getOrder: returning order ' + str(order_to_return))
            return order_to_return
        else: 
            # Error handling 
            logging.debug('[OrderManagementServicer] getOrder: Order not found ' + request.value)

            # Usare set_code() per impostare il valore da usare come status code quando la RPC completa con errore
            # per gli StatusCode vedere: https://grpc.github.io/grpc/python/_modules/grpc.html#StatusCode

            context.set_code(grpc.StatusCode.NOT_FOUND)

            # Usare set_details() per impostare il valore da usare come stringa di dettaglio quando la RPC completa
            # con errore.

            context.set_details('Order : ', request.value, ' Not Found.')

            # ritorno un Order vuoto in caso di errore
            return order_management_pb2.Order()


    # Unary RPC
    def addOrder(self, request, context):
        id = uuid.uuid1() # Used to generate a uniqe id from the MAC address
        request.id = str(id)
        
        ## creo l'item come dict da aggiungere al db in base alla richiesta dal client
        order_dict_db = {'id': request.id,
                                'items': list(request.items), ## il repeated in protobuf può essere convertito in lista esplicitamente con list
                                'description': request.description,
                                'price' : request.price,
                                'destination': request.destination
                                }

        ## aggiungo l'ordine al db usando insert_one()
        self.orders_collection.insert_one(order_dict_db)

        response = order_management_pb2.StringMessage(value=str(id))
        
        logging.debug('[OrderManagementServicer] addOrder: addedd order with ID: ' + str(id))
        return response


    # Server Streaming 
    def searchOrders(self, request, context):  
        logging.debug('[OrderManagementServicer] searchOrders: searching for orders with item equal to: ' + request.value)

        orders_db_find = self.orders_collection.find({"items" : {"$in" : [request.value]}})

        for order_el in orders_db_find:
            
            order_to_return = order_management_pb2.Order(id=order_el['id'],
                                                        items=order_el['items'],
                                                        description=order_el['description'],
                                                        price=order_el['price'],
                                                        destination=order_el['destination'])

            yield order_to_return

        #matching_orders = self.searchInventory(request.value)
        #for order in matching_orders:
        #    yield order


    # Bi-di Streaming 
    def processOrders(self, request_iterator, context):
        
        logging.debug('[OrderManagementServicer] processOrders: processing orders for shipping...')

        location_dict = {}

        ### lo stream di richieste di ordini potrebbe essere modificato invocando la addOrder
        
        """
        organizzo gli ordini per destination in modo da creare un location_dict:
        
        location_dict sarà una cosa del genere:

            {'San Jose, CA': 
                [
                    {
                        id: "3632b44c-0c94-11ef-bf4b-acde48001122"
                        items: ["Item - A", "Item - B", "Item - C"]
                        description: "This is a Sample order - 1 : description."
                        price: 2450.5
                        destination: "San Jose, CA"
                    },
                    {   
                        id: "3632b44c-0c94-11ef-bf4b-acde48001123"
                        items: ["Item - A", "Item - B"]
                        description: "This is a Sample order - 1 : description."
                        price: 2410.5
                        destination: "San Jose, CA"
                }]
            }
        """    
        
        for order in request_iterator:
            
            ## aggiungo gli ordini al magazzino
            self.addOrder(order, context)

            ### creo il dict relativo all'Order in modo da memorizzarlo su mongodb successivamente insieme all'oggetto shipment
            order_dict = {
                                'id' : order.id,
                                'items': list(order.items),
                                'description': order.description,
                                'price': order.price,
                                'destination': order.destination
                                }

            if order.destination not in location_dict.keys(): ## se è la prima volta che aggiungo quella chiave
                location_dict[order.destination] = [order_dict]
            else:
                location_dict[order.destination].append(order_dict)
            
        ### dato il location_dict devo costruire un altro dict per lo shipment in modo da porterlo memorizzare
        ### su mongodb
        
        for destination, orders in location_dict.items():

            shipment_id = str(uuid.uuid1())

            ## creo l'item di shipment come dict da aggiungere al db 
            ## la lista degli ordini è già una lista di dict che mappano tutti gli Order
            
            shipment_dict_db = {
                                'id': shipment_id,
                                'status' : "PROCESSED",
                                'orders' : orders
                                }
            
            logging.debug("[OrderManagementServicer] processOrders: shipment_dict_db: " + str(shipment_dict_db))
            ## aggiungo l'ordine al db usando insert_one()
            self.shipment_collection.insert_one(shipment_dict_db)
           
            # la lista degli ordini (orders) è una lista di dict che viene serializzata automaticamente da grpc
            shipment = order_management_pb2.CombinedShipment(id=str(shipment_id), status='PROCESSED', orders=orders)
            
            yield shipment
            logging.debug('[OrderManagementServicer] processOrders: processed shipment: ' + str(shipment_id))

        logging.debug('[OrderManagementServicer] processOrders: processing orders completed!')

    def cancelShipment(self, request, context):

        self.shipment_collection.delete_one({"id": request.value})

        return order_management_pb2.StringMessage(value="DELETED")
    

def serve(orders_collection, shipment_collection):
    # Creating gRPC Server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(orders_collection, shipment_collection), server)

    port = 0 # with port = 0,  the gRPC runtime will choose a port

    port = server.add_insecure_port('[::]:' + str(port)) 
    logging.debug('Starting OrderManagement server. Listening on port ' + str(port))

    server.start()

    server.wait_for_termination()



def get_database():
 
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://127.0.0.1:27017"
 
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['OrderManagementDB']
  
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    
    ## prendo il ref del document mongodb
    db = get_database()
    print(db)
    
    ## prendo i ref delle collection orders e shipments
    orders_collection = db["orders"]
    shipment_collection = db["shipments"]
    
    print(orders_collection)
    print(shipment_collection)
    
    serve(orders_collection, shipment_collection)