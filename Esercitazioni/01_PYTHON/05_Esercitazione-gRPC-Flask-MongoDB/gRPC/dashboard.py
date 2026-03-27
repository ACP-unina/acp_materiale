import sys
import grpc
import statistics_pb2, statistics_pb2_grpc

def run(port):

    # Creo il canale gRPC
    channel = grpc.insecure_channel('localhost:' + str(port))

    # Ottengo lo stub
    stub = statistics_pb2_grpc.StatisticsManagerStub(channel)

    # Recupero i sensori disponibili
    print('[DASHBORAD] Sending request for availabe sensors')
    sensors_response = stub.getSensors(statistics_pb2.Empty())

    sensors = []
    
    print('[DASHBORAD] Available sensors:')
    for sensor in sensors_response:
        print(f'[DASHBORAD]   sensor_id: {sensor.sensor_id} - data_type: {sensor.data_type}')
        sensors.append(sensor)
    
    # Itero sui sensori
    for sensor in sensors:

        # Richiedo il calcolo della la media per uno dei sensori
        print(f'[DASHBORAD] Sending mean request:  sensor_id: {sensor.sensor_id} - data_type: {sensor.data_type}')
        response = stub.getMean(statistics_pb2.MeanRequest(sensor_id=sensor.sensor_id, data_type=sensor.data_type))

        print(f'[DASHBOARD]     Mean: {response.value}')


# Start client
if __name__ == "__main__":

    try:
        port = sys.argv[1]
    except IndexError:
        print("Please, specify PORT arg...")

    run(port)