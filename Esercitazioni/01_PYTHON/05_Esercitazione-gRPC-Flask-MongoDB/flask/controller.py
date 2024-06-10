from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

# Get the database
def get_database():

    client = MongoClient("127.0.0.1", 27017)

    return client['sensors_data']


# curl -X POST --json '{"sensor_id":10, "data":35}' http://127.0.0.1:5000/data/temp
# curl -X POST --json '{"sensor_id":10, "data":35}' http://127.0.0.1:5000/data/press
@app.post('/data/<data_type>')
def store_data(data_type):

    '''
    try:
        body = request.get_json()

        id = body['id']
        data = body['data']

    except KeyError:
        print("[STORE TEMP DATA] Bad reuqest")
        return {result: "FAILURE"}, 400
    '''

    # Ottengo già un dizionario dalla get_json, quindi non ho bisogno di trasformazioni
    # Non faccio check sui campi, per avere flessibilità sul formato dati (dato l'utilizzo di un NoSQL database)
    body = request.get_json()

    # Richiedo la connessione al DB
    db = get_database()

    # Accedo alla collection in base al parametro type
    if data_type == "temp":
        data_collection = db['temp_data']
    elif data_type == "press":
        data_collection = db['press_data']
    else:
        return {'result' : 'Unsupported data type'}, 400
    
    # Effettuo l'inserimento del document nella collection
    try:
        data_collection.insert_one(body)
    except Exception as e: 
        print("[STORE DATA] Operation failed")
        return {'result': 'failed - ' + str(e)}, 500
    else:
        print("[STORE DATA]", data_type, "data saved on DB")
        return {'result': 'success'}


# curl -X POST --json '{"_id":10, "data_type":"temp"}' http://127.0.0.1:5000/sensor/
# curl -X POST --json '{"_id":20, "data_type":"press"}' http://127.0.0.1:5000/sensor/
@app.post('/sensor')
def add_sensor():

    # Ottengo già un dizionario dalla get_json, quindi non ho bisogno di trasformazioni
    # Non faccio check sui campi, per avere flessibilità sul formato dati (dato l'utilizzo di un NoSQL database)
    body = request.get_json()

    # Richiedo la connessione al DB
    db = get_database()

    sensor_collection = db['sensors']

    result = None
    # Effettuo l'inserimento del document nella collection
    try:
        result = sensor_collection.insert_one(body)
    except Exception as e:  
        print("[ADD SEONSOR] Operation failed")
        return {'result': 'failed - ' + str(e)}, 500
    else:
        print("[ADD SENSOR] Added new sensor")
        return {'result': 'success'}



if __name__  == "__main__":

    app.run(debug=True, port=5001)

    
