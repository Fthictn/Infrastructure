import json
import flask
import requests
from requests.auth import HTTPBasicAuth
from InternalSettings import InternalSettings

app = flask.Flask(__name__)
app.config["DEBUG"] = True

BASE_URL = "http://localhost:8075"


@app.route('/getInternalSettings', methods=['GET'])
def getInternalSettings():
    url = BASE_URL + "/internalSettings"
    response = requests.get(url=url, auth=HTTPBasicAuth('Administrator', '123456'))
    response = json.loads(json.dumps(response.json()))
    internalSettings = InternalSettings(**response)
    return json.dumps(internalSettings._asdict())


app.run()
