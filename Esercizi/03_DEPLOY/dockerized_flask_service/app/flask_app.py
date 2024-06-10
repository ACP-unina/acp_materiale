# flask_app.py
from flask import Flask, request
import socket

app = Flask(__name__)

@app.route("/")
def index():
	return "This is an example Flask app served from {} to {}".format(socket.gethostname(), request.remote_addr)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5001, debug=True)
