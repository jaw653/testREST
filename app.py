"""
Author: Jake Wachs
Test RESTful API

12/7/2019
"""

from helpers import *

from flask import Flask, Response, request, render_template, \
    make_response, jsonify, json
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

app = Flask('app')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'   # Enable CORS


'''
BEGIN CLIENTSIDE ROUTES
'''
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    Basic home page for testing requests
    """
    return render_template('index.html')


@app.route('/register',  methods=['GET', 'POST'])
def register():
    """
    Registration page
    """
    return render_template('register.html')


@app.errorhandler(404)          # FIXME: makea a better not found page
def notfound(e):
    """
    Handle a page not being found
    """
    return '<h1>page not found</h1>'


'''
BEGIN API ENDPOINTS
'''
@app.route('/api/v1/users', methods=['GET', 'POST'])
def handleRegistration():
    """
    A simple test endpoint
    """
    # Setup database connection
    collection = MongoClient().test.users

    if request.method == 'POST':
        # Get the JSON from the request and create dump for response
        content = request.get_json()
        dump = json.dumps(content)

        # Create new user object for easy manipulation & insert to mongo
        newUser = createNewUser(content)
        newUser.insertDB(collection)
        print('New user, ' + newUser.getUsername() + ', created!')

        return Response(dump, status=201, mimetype='application/json')

    elif request.method == 'GET':
        # Get cursor of all users in collection
        users = collection.find()

        # Manually create python dictionary for conversion to JSON
        userList = createDict(users)

        return Response(json.dumps(userList, indent=4, separators=(',', ': ')),\
            status=200, mimetype='application/json')

    return render_template('endpoint.html')


'''
BEGIN MAIN
'''
if __name__ == '__main__':
    app.run(threaded=True, debug=True, \
        host='0.0.0.0', port=5000)
