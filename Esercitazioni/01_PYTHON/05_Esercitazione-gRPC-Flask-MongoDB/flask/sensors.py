import requests, random
import threading as mt

supported_types = ['temp', 'press']
server_address = "http://127.0.0.1:5001"

NUM_REQUS = 5

def thread_fun(sensor_id):

    # Selezioni in maniera casuale il data type
    data_type = supported_types[random.randint(0, 1)]

    # Preparo la richiesta per l'inserimento del sensore lato controller
    sensor_spec = {
        '_id' : sensor_id,
        'data_type': data_type
    }

    # Preparo la url per la richiesta
    resourse_location = server_address + "/sensor"

    # Invio la richiesta su /sensor
    response = requests.post(resourse_location, json=sensor_spec)

    # Gestisco eventuali errori
    try:

        response.raise_for_status()

    except requests.exceptions.HTTPError:
        print(f"[SENSOR-{sensor_id}] Error: Received {response.status_code} - {response.text}")
    else:
        print(f"[SENSOR-{sensor_id}] Added sensor with: {sensor_spec}")


    # Generazione di richieste multiple verso /data/<data_type>
    for i in range (NUM_REQUS):

        # Generao i dati da inviare
        data = {
            'sensor_id' : sensor_id,
            'data' : random.randint(1, 50)
        }
    
        # Preparo la url per la richiesta
        resourse_location = server_address + "/data/" + data_type

        # Invio la richiesta su /data/<data_type>
        response = requests.post(resourse_location, json=data)

        # Festisco eventuali errori
        try:

            response.raise_for_status()

        except requests.exceptions.HTTPError:
            print(f"[SENSOR-{sensor_id}] Error: Received {response.status_code} - {response.text}")
        else:
            print(f"[SENSOR-{sensor_id}] Added {data_type} data: {data}")


if __name__ == "__main__":

    threads = []
    
    # Avvio i thread
    for i in range(1, 6):

        thd = mt.Thread(target=thread_fun, args=(i,))
        thd.start()
        threads.append(thd)

    for thread in threads:
        thread.join()


