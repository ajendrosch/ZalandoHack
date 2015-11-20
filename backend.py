from flask import Flask, request
from flask.ext.cors import CORS

import json

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route("/upload", methods=['POST'])
def upload():
    img  = request.form['img']
    return img

if __name__ == "__main__":
    app.run(port=80)
