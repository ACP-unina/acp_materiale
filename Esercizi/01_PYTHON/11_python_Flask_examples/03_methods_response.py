from flask import Flask, request, make_response
import random, time

app = Flask(__name__)

# Manage multiple methods
# test GET: curl http://127.0.0.1:5000/print
# test POST: curl -X POST http://127.0.0.1:5000/print
@app.route('/print', methods=['GET', 'POST'])
def print_method():

   if request.method == 'POST':
      return '<h1>This is a POST</h1>'
   else:
      return '<h1>This is a GET</h1>'

# Manage GET requests
# test: curl http://127.0.0.1:5000/print2
@app.get('/print2')
def print_get():
    return '<h1>This is a GET</h1>'

# Manage POST requests
# test: curl -X POST http://127.0.0.1:5000/print2
@app.post('/print2')
def print_post():
    return '<h1>This is a POST</h1>'

# Support function
def get_all_users():

    usernames = ['pippo', 'pluto', 'pippozzo', 'plutozzo']
    users = []

    for usename in usernames:

        users.append({'username': usernames.pop(), 'age': random.randint(18, 99)})

    return users

# Return a dictionary in JSON format
@app.route("/me")
def me_api():
   user = {
      "username": "pippo",
      "age": 20
   }
   return user #### user è un dict ma il ritorno è jsonificato! application/json (VEDERE STRUMENTI PER SVILUPPATORI)

# Return a list in JSON format
@app.route("/users")
def users_api():
   users = get_all_users() #return a list of dictionaries
   return users

# Return a tuple in the format (response, status)
@app.route('/error')
def error():
   return '<h1>Bad Request</h1>', 400

# Return a tuple in the format (response, status)
@app.route('/errorh')
def errorh():
    headers = {'New header' : 'Flask Application'}
    return '<h1>Bad Request</h1>', 400, headers

# Make a Response object within the view function
@app.route('/make')
def make():
   response = make_response('<h1>This document carries a cookie!</h1>')
   response.set_cookie('Last-access', str(time.time()))
   return response



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
