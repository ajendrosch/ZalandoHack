from flask import Flask, request

import json
import base64


app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    img  = request.form['img']
    img = img.split(",")[1]
    fh = open("imageToSave.png", "wb")
    fh.write(img.decode('base64'))
    fh.close()
    data = {}
    data["result"] = "test"
    return json.dumps(data)

if __name__ == "__main__":
    app.run(port=80)




    
