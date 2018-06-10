from flask import Flask
from flask import request
from flask import make_response,Response
import json

app = Flask(__name__)

import json
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
app = Flask(__name__)







@app.route('/test' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST' :
	    
         a = request.get_data()
         
         data = {
		"returnCode": "0",
		"returnErrorSolution": "",
		"returnMessage": "",
		"returnValue": {
		"reply": "",
		"resultType": "RESULT",
		"actions": [{
			"name": "audioPlayGenieSource",
			"properties": {
				"audioGenieId": "123"
			}
		}],
		"properties": {},
		"executeCode": "SUCCESS",
		"msgInfo": ""
		}
		}
         
         dict1 = json.loads(a.decode('utf-8'))
 
         #print (dict1["intentId"])
         if str(dict1["utterance"]) == "广多":
            #a = content['pc']['age']
            data['returnValue']['reply'] = "哈哈"
         #print (dict1)
    #print (a)
		#####python中包含UTF-8编码中文的列表或字典的输出
		###print json.dumps(dict, encoding="UTF-8", ensure_ascii=False)
			#return json.dumps(dict1,ensure_ascii=False)
            return json.dumps(data,ensure_ascii=False)
         else:
              data['returnValue']['reply'] = "88"
              print ('no')
              return json.dumps(data,ensure_ascii=False)
			



if __name__ == '__main__':
          app.run(
        host = '0.0.0.0',
        port = 7777,
        debug = True
    )
