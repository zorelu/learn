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
##获取所有post过来的json格式
@app.route('/test' , methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
         a = request.get_data()

         dict1 = json.loads(a.decode('utf-8'))
		 ##获取某个json字段
         print (dict1["intentId"])
		 
         print (dict1)
    #print (a)
		#####python中包含UTF-8编码中文的列表或字典的输出
		###print json.dumps(dict, encoding="UTF-8", ensure_ascii=False)
		###需改系统默认编码为zh_CN.UTF-8
         return json.dumps(dict1,ensure_ascii=False)
    else:
        return '<h1>111</h1>'



if __name__ == '__main__':
          app.run(
        host = '0.0.0.0',
        port = 7777,
        debug = True
    )
	
export LANG=zh_CN:UTF-8 export LANGUAGE=zh_CN:en
