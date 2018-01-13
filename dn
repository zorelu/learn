from flask import send_file, send_from_directory
from flask import Flask, session, redirect, url_for, escape, request
import os

app = Flask(__name__)
#post方法
@app.route("/download/", methods=['post'])
def download_file():
    ##获取当前目录
    directory = os.getcwd()
    #name = "index.html"
    request.method == 'POST'
    name1 = request.form['filename']
    ##后缀名
    name = name1 + ".tar.gz"
    #print(name)
    return send_from_directory(directory, name, as_attachment=True)
    #return '%s' % name1
    
app.run(host='0.0.0.0')


###附上对应的html demo 需要放在同一个目录

<form action="http://web.94linux.com:5000/download/" method="post">
  <p>filenaem: <input type="date" name="filename" /></p>
  <input type="submit" value="download" />
</form>
cat: h: No such file or directory
