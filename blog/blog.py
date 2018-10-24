from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    # remove the username from the session if it's there

    return render_template('index.html')


app.run(host='127.0.0.1')