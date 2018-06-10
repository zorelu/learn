import time
import datetime
from pymongo import MongoClient
import json
import requests
import pymssql
from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)


data ={
    "returnCode": "0",
    "returnErrorSolution": "",
    "returnMessage": "",
    "returnValue": {
        "reply": "哈哈哈",
        "resultType": "RESULT",
        "actions": [
            {
                "name": "audioPlayGenieSource",
                "properties": {
                    "audioGenieId": "123"
                }
            }
        ],
        "properties": {},
        "executeCode": "SUCCESS",
        "msgInfo": ""
    }
}
# post方法est
@app.route("/test", methods=['GET', 'POST'])
def test():
    #request.method == 'POST'
    return json.dumps(data)


#print (data)


app.run(host='0.0.0.0')