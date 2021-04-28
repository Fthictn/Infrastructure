import flask
import requests
from flask import request, jsonify
from requests.auth import HTTPBasicAuth

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/getAlerts', methods=['GET'])
def getalerts():
    URL = "http://localhost:8065/settings/alerts"
    r = requests.get(url=URL, auth=HTTPBasicAuth('Administrator', '123456'))
    return jsonify(r.json())


@app.route('/', methods=['GET'])
def getBooks():
    return None


app.run()
