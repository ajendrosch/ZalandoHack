from flask import Flask, request
from flask.ext.cors import CORS

import json

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['img']
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

if __name__ == "__main__":
    app.run(port=80)
