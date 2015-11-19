from flask import Flask, request
from flask.ext.cors import CORS

import json

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=['POST'])
def upload():
    return request.form['img']

if __name__ == "__main__":
    app.run(port=80)
