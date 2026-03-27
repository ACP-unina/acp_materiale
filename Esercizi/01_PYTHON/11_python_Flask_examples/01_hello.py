# hello.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/user/<name>')
def user(name):
 return '<giggino>Hello, %s!' % name

if __name__ == "__main__":
    #app.run(debug=True)
   	app.run(host='0.0.0.0', port=5001, debug=True)


