import os
import sys
import json

from flask import Flask, request, session, redirect, jsonify
from flask_cors import CORS

import helpers


#-Global Vars---------------------------------------------------------
curPath = os.path.dirname(os.path.abspath(__file__))
print(curPath)


#-Build the flask app object---------------------------------------
app = Flask(__name__)
app.secret_key = "changeit"
app.debug = True
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#-The APP Request Handler Area-------------------------------------

@app.route('/', methods=['GET'])
def app_home():
  return "<h2>Hallo from the App</h2>"

#------------------------------------------
@app.route('/api', methods=['GET'])
def api_home():
  testObj = {
    "path": "/api",
    "status": 200,
    "message": "Hello from the API"
  }
  return jsonify(testObj), 200



#-App Runner------------------------------------------------------
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)

#------------------------------------------------------------------