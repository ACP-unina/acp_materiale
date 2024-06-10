import grpc
import statistics_pb2
import statistics_pb2_grpc
from pymongo import MongoClient

from concurrent import futures 


# Get the database
def get_database():

    client = MongoClient("127.0.0.1", 27017)

    return client['sensors_data']

    
class StatisticsServicer(statistics_pb2_grpc.StatisticsManagerServicer):

    def __init__(self, db):

        self.db = db
    
    # Prevede in input un messaggio Empty e ritorna un Sensors
    # RPC streaming server
    def getSensors(self, request, context):

        print("[GET SENSORS] Getting the sensors from db")

        # Recupero la collection con i sensori
        sensor_collection = self.db['sensors']
        
        sensor_ids = []
        data_types = []

        # Recupero i dati dalla collection
        results = sensor_collection.find({})

        # Genero le liste da includere nel messaggio Sensors da rtitornare
        for result in results:
            
            print("[GET SENSORS] Get sensor: " + str(result))

            # Gestisco il caso di campi non presenti per alcuni document
            try:
                sensor_id = result['_id']
                data_type = result['data_type']

            except Exception as e:

                print("[GET SENSORS] Failed retrieving one of the required field...skipping the data")
                print("[GET SENSORS] Obtaianed - " + str(result))
                continue

            yield statistics_pb2.Sensor(sensor_id=sensor_id, data_type=data_type)


    # Prevede in input un MeanRequest e ritorna uno StringMessage (in cui inserire la media)
    # RPC unary
    def getMean(self, request, context):

        # Estraggo sensor_id e data_type da MeanRequest
        sensor_id = request.sensor_id
        data_type = request.data_type

        print(f"[GET MEAN] Recevied request for sensord_id: {sensor_id} - data_type: {data_type}")

        collection = None

        # Recupero la collection in base al data_type presente nella Mean Request
        if data_type == "temp":
            
            collection = self.db['temp_data']

        elif data_type == "press":

            collection = self.db['press_data']
        
        else:

            return statistics_pb2.StringMessage(value='-1')

        # Recupero i dati dalla collection, filtrandoli in base al sensor_id
        results = collection.find({'sensor_id':sensor_id})

        mean = 0
        elem = 0
        
        # Itero sui risultati per calcolare la media
        for result in results:
            try:
                mean = mean + result['data']
                elem = elem + 1
            except Exception as e:
                print("[GET MEAN] Failed retrieving one of the required field...skipping the data")
                print("[GET MEAN] Obtaianed - " + str(result))
                continue

        mean = mean / elem

        print("[GET MEAN] The mean is: " + str(mean))

        return statistics_pb2.StringMessage(value=str(mean))



if __name__ == "__main__":

    db = get_database()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),))
    statistics_pb2_grpc.add_StatisticsManagerServicer_to_server(StatisticsServicer(db), server)

    port = 0 

    port = server.add_insecure_port('[::]:' + str(port)) 
    print('Starting server. Listening on port ' + str(port))

    server.start()

    server.wait_for_termination()