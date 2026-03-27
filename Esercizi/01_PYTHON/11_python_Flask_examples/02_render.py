# hello-render.py
from flask import Flask, render_template, request
import os

#app = Flask(__name__)
template_dir = os.path.abspath('./02_templates/')
app = Flask(__name__, template_folder=template_dir)


@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/user_adv/<name>')
def user_adv(name):
    if name == "pippo":
        return render_template('user_adv.html', name=name, elements=['String', 10, {'key':'value'}])
    else:    
        return render_template('user_adv.html')

@app.route('/user_agent')
def user_agent():
    user_agent = request.headers.get('User-Agent')
    return user_agent

# test: curl --json '{"text":"prova"}' http://127.0.0.1:5000/json
# N.B.: --json doesn't work on Mac OSX
# test: curl -H "Content-Type: application/json" '{"text":"prova"}' http://127.0.0.1:5000/json
@app.post('/json')
def json():
   json = request.get_json()
   print(json)
   return json

# test: curl -d 'prova' http://127.0.0.1:5000/data
@app.post('/data')
def data():
   data = request.get_data(as_text=True)
   print(data)
   return data

# test: curl "http://127.0.0.1:5000/hello?name=pippo&surname=pippozzo"
@app.get('/hello')
def hello():
   params = request.args
   print("name:", params['name'])       
   print("surname:", params['surname']) 
   return params

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5001, debug=True)




