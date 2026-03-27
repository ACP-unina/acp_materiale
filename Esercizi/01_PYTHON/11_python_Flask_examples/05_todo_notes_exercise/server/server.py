from flask import Flask, request
import uuid

app = Flask(__name__)

notes = {}


# test: curl --json '{"text":"prova", "tag":"work"}' http://127.0.0.1:5000/note
@app.post('/note')
def add_note():

    try:
        
        text = request.get_json()['text']
        tag = request.get_json()['tag']

    except KeyError:
        print("[ADD] Bad format")
        ### il ritorno è un dict che viene jsonificato
        return {"result": "Bad format of the request", "id": -1}, 400 
    
    print("[ADD] Received note:", text, "with tag:", tag)

    id = uuid.uuid4().hex

    notes[id] = request.get_json()

    return {"result": "added", "id": id}


# test: curl http://127.0.0.1:5000/note/a9d6404d32054e95ad8e9f14a4a94fb2
# Sostituire l'id con uno valido
@app.get('/note/<id>')
def get_note(id):

    print("[GET NOTE] Received id:", id)
    try:
        response = notes[id]
    except KeyError:
        print("[GET NOTE] Note not found")
        return {"result": "Note not found"}, 404

    return response

 
# test: curl http://127.0.0.1:5000/notes
@app.get("/notes")
def get_notes():

    print("[GET NOTES] Received request")
    result = []
    for id, note in notes.items():
        result.append({"id": id, "note": note})

    return result


# test: curl -X PUT --json '{"text":"modified", "tag":"sport"}' http://127.0.0.1:5000/note/a9d6404d32054e95ad8e9f14a4a94fb2
# Sostituire l'id con uno valido
@app.route("/note/<id>", methods=['PUT']) # potrebbe essere utilizzato anche @app.put("/note/<id>")
def update_note(id):

    msg = "updated"
    try:
        text = request.get_json()['text']
        tag = request.get_json()['tag']
    except KeyError:
        print("[UPDATE] Bad format")
        return {"result": "Bad format of the request", "id": -1}, 400 
    
    print("[UPDATE] Received note:", text, "with tag:", tag)

    try:
        print("[UPDATE] Current note:", notes[id])
    except KeyError:
        print("[UPDATE] The not does not exist - a new one will be created")
        msg = "added"
        
    
    notes[id] = request.get_json()

    return {"result": msg, "id": id}


# test: curl -X DELETE http://127.0.0.1:5000/note/1a8a770a9b9d4783a7ff5f9f8151558e
# Sostituire l'id con uno valido
@app.delete("/note/<id>")
def del_note(id):

    print("[DEL NOTE] Received id:", id)
    try:
        response = notes.pop(id)
    except KeyError:
        print("[DEL NOTE] Note not found")
        return {"result": "Note not found"}, 404

    return {"result": "deleted", "id": id}


# test: curl -X DELETE http://127.0.0.1:5000/notes
@app.delete("/notes")
def del_notes():

    print("[DEL NOTES] Received request")
    
    notes.clear()

    return {"result": "No more notes"}




if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5001, debug=True)
    




