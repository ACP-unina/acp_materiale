import grpc
import order_management_pb2
import order_management_pb2_grpc

import multiprocess as mp

import time
import sys
import logging


def run(port):

    # mi creo il canale per la comuniziona con il servizio OrderManagement specificando il porto
    channel = grpc.insecure_channel('localhost:' + str(port))

    # mi creo lo stub client per invocare i metodi remoti
    stub = order_management_pb2_grpc.OrderManagementStub(channel)

    # creo una lista di 5 ordini lato client
    orders = []

    orders.append(order_management_pb2.Order(price=2450.50,
                                        items=['Item - A', 'Item - B', 'Item - C'],
                                        description='This is a Sample order - 1 : description.', 
                                        destination='San Jose, CA'))

    orders.append(order_management_pb2.Order(price=1000, 
                                        items=['Item - A', 'Item - B'], 
                                        description='Sample order description.',
                                        destination='Naples'))
    
    orders.append(order_management_pb2.Order(price=1000, 
                                        items=['Item - C'], 
                                        description='Sample order description.',
                                        destination='Rome'))

    orders.append(order_management_pb2.Order(price=1000, 
                                        items=['Item - A', 'Item - E'], 
                                        description='Sample order description.',
                                        destination='Milan'))
    
    orders.append(order_management_pb2.Order(price=1000, 
                                        items=['Item - F', 'Item - G'], 
                                        description='Sample order description.'))   

    print("############")
    # 1. Mando all'OrderManager i 5 ordini attraverso l'invocazione di addOrder che mi restituisce l'ID generato dal manager
    # Uso getOrder per ottenere l'order a partire dal suo ID

    for order in orders:

        # Unary RPC : Adding an Order
        response = stub.addOrder(order)
        print('addOrder() invoked. Response :', response)

        # Unary RPC : Getting an Order 
        order = stub.getOrder(response)
        print("getOrder() invoked. Response: ", order)

    # 2. Ricerca di un particolare item aggiunto ad uno degli ordini precedentemente inviati al Manager, 
    # stampando la lista di ordini che contiene quell’item.

    # Server-side Streaming
    # La funzione searchOrders mi restituisce uno stream di messaggi di tipo Order
    print("############")
    order_search_result = stub.searchOrders(order_management_pb2.StringMessage(value='Item - A'))
    print('searchOrders("Item - A") invoked. Result:')
    for order in order_search_result:
        print(order)

    # 3. crea 4 ordini, due dei quali hanno la stessa destinazione, 
    # e richiede al Manager la creazione delle relative spedizioni attraverso la processOrders

    # Bi-di Streaming 
    print("############")
    proc_order_iterator = generate_orders_for_processing()
    
    shipments = stub.processOrders(proc_order_iterator)
    print("processOrders() invoked. Results: \n")
    for shipment in shipments:
        print('Shipment : ', shipment)

    

def generate_orders_for_processing():

    print("Generating orders to delivery...")

    ord1 = order_management_pb2.Order(
        id='104', price=2332,
        items=['Item - A', 'Item - B'],  
        description='Updated desc', 
        destination='San Jose, CA')
    
    ord2 = order_management_pb2.Order(
        id='105', price=3000, 
        description='Updated desc', 
        destination='San Francisco, CA')
    
    ord3 = order_management_pb2.Order(
        id='106', price=2560, 
        description='Updated desc', 
        destination='San Francisco, CA')
    
    ord4 = order_management_pb2.Order(
        id='107', price=2560, 
        description='Updated desc', 
        destination='Mountain View, CA')
    
    list = []
    list.append(ord1)
    list.append(ord2)
    list.append(ord3)
    list.append(ord4)

    for processing_orders in list:
        yield processing_orders


# Start client
if __name__ == "__main__":

    try:
        port = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg...")

    logging.basicConfig()
    run(port)