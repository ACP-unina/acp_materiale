from concurrent import futures
import time
import uuid
import sys

import grpc
import order_management_pb2_grpc
import order_management_pb2

import logging

class OrderManagementServicer(order_management_pb2_grpc.OrderManagementServicer): 

    def __init__(self):
        
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
        self.orderDict = {}                                                          

    # Unary RPC
    def getOrder(self, request, context):
        order = self.orderDict.get(request.value)
        if order is not None: 
            logging.debug('[OrderManagementServicer] getOrder: returning order ' + str(order))
            return order
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
        self.orderDict[request.id] = request
        response = order_management_pb2.StringMessage(value=str(id))
        #print(self.orderDict)
        #types_keys = [type(k) for k in self.orderDict.keys()]
        #types_values = [type(k) for k in self.orderDict.values()]
        #print(types_keys)
        #print(types_values)
        logging.debug('[OrderManagementServicer] addOrder: addedd order with ID: ' + str(id))
        return response


    # Server Streaming 
    def searchOrders(self, request, context):  
        logging.debug('[OrderManagementServicer] searchOrders: searching for orders with item equal to: ' + request.value)
        matching_orders = self.searchInventory(request.value)
        for order in matching_orders:
            yield order


    # Bi-di Streaming 
    def processOrders(self, request_iterator, context):
        
        logging.debug('[OrderManagementServicer] processOrders: processing orders for shipping...')

        location_dict = {}

        for order in request_iterator:

            if order.destination not in location_dict.keys():
                location_dict[order.destination] = [order]
                #print(location_dict[order.destination])
                
            else:
                """
                {'Napoli': [
                    id: "3632b44c-0c94-11ef-bf4b-acde48001122"
                items: "Item - A"
                items: "Item - B"
                items: "Item - C"
                description: "This is a Sample order - 1 : description."
                price: 2450.5
                destination: "San Jose, CA"
                
                id: "3632b44c-0c94-11ef-bf4b-acde48001122"
                items: "Item - A"
                items: "Item - B"
                items: "Item - C"
                description: "This is a Sample order - 1 : description."
                price: 2450.5
                destination: "San Jose, CA"]
                }
                """
                #lista_ordini = location_dict[order.destination]
                #lista_ordini.append(order)
                location_dict[order.destination].append(order)
                #print(location_dict[order.destination])
                
            
        
        for key, values in location_dict.items():

            shipment_id = uuid.uuid1()
            shipment = order_management_pb2.CombinedShipment(id=str(shipment_id), status='PROCESSED', orders=location_dict[key])
            # shipment = order_management_pb2.CombinedShipment(id=str(shipment_id), status='PROCESSED', orders=values) ### EQUIVALENTE
            
            yield shipment
            logging.debug('[OrderManagementServicer] processOrders: processed shipment: ' + str(shipment_id))

        logging.debug('[OrderManagementServicer] processOrders: processing orders completed!')


    # Local function 
    def searchInventory(self, query):
        matchingOrders = []    
        for order_id, order in self.orderDict.items(): 
            for itm in order.items:
                if query in itm:
                    matchingOrders.append(order)
                    break
        return matchingOrders
 

def serve():
    # Creating gRPC Server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),))
    order_management_pb2_grpc.add_OrderManagementServicer_to_server(OrderManagementServicer(), server)

    port = 0 # with port = 0,  the gRPC runtime will choose a port

    port = server.add_insecure_port('[::]:' + str(port)) 
    logging.debug('Starting server. Listening on port ' + str(port))

    server.start()

    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    serve()