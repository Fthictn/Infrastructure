import json
import flask
import requests
from flask import jsonify
from requests.auth import HTTPBasicAuth
from InternalSettings import InternalSettings
from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator

app = flask.Flask(__name__)
app.config["DEBUG"] = True

BASE_URL = "http://localhost:8075"


@app.route('/getInternalSettings', methods=['GET'])
def getInternalSettings():
    url = BASE_URL + "/internalSettings"
    response = requests.get(url=url, auth=HTTPBasicAuth('Administrator', '123456'))
    jsonString = json.loads(json.dumps(response.json()))
    internalSettings = InternalSettings(**jsonString)
    return json.dumps(internalSettings._asdict())


@app.route('/getEmployee', methods=['GET'])
def getEmployee():
    cluster = Cluster('couchbase://172.17.0.4', authenticator=PasswordAuthenticator('Administrator', '123456'))
    employee = cluster.bucket('employee')
    coll = employee.default_collection()
    employeeDoc = {
        "name": "Eda",
        "surname": "Şahinli"
    }
    coll.upsert("employee1", employeeDoc)
    result = coll.get("employee1")
    return jsonify(result.content_as[str])


app.run()
