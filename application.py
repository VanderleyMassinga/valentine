import datetime

from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    valentine_day = now.month == 2 and now.today == 14
    return render_template("index.html", valentine_day=valentine_day)