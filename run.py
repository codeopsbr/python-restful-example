import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the example application."

if __name__ == "__main__":
    app.run(debug = "True")