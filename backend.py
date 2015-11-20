from metamind.api import ClassificationData, ClassificationModel, set_api_key
from flask import Flask, request
import json
from flask.ext.cors import CORS

set_api_key('nDdCYFXwkFPp8b0O2L7aQRmY7aOfdnOtSodaHP3rA9eIKXqhqe')

classifier = ClassificationModel(id='40323')

final=[
('http://www.mensflair.com/media/michael-jackson-style.jpg', 'michael jackson'),
('https://s-media-cache-ak0.pinimg.com/236x/6c/59/4b/6c594b12af3e0aca0f56282c906b9893.jpg', 'Matthew Perry'),
                           ('http://celebmafia.com/wp-content/uploads/2015/06/taylor-swift-style-at-lax-airport-june-2015_5.jpg', 'Taylor swift'),

                           
                           
                           ('http://i.dailymail.co.uk/i/pix/2015/05/12/16/2892A11600000578-0-image-m-10_1431445560818.jpg', 'David Schimmer'),

                           
                           
                           ('https://s-media-cache-ak0.pinimg.com/736x/0d/00/fb/0d00fb105c433ff431cfc5031ffd372c.jpg','jim parson'),

                           
                           
                           ('http://celebritiestown.com/celebritypictures/var/albums/Anne-Hathaway-style-Brooklyn/anne-hathaway-style-02.jpg', 'Anna Hathway'),

                           
                           
                           ('http://www.itslavida.com/files/2014/07/Smart-Casual.jpg','david beckham'),

                           
                           
                            ('http://assets.elleuk.com/gallery/16537/1397671324-victoria-beckham-february-10-2014-nyc-getty__large.jpg','viktoria beckham'),

                           
                           
                           ('http://latestreviewz.com/wp-content/uploads/2015/01/Celebrity-Jackie-Chan-Dressing-Style-Hairstyles-7.jpg','Jackie chan')

                           
                     ]

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=['POST'])
def upload():
    img  = request.form['img']
    img = img.split(",")[1]
    fh = open("imageToSave.png", "wb")
    fh.write(img.decode('base64'))
    fh.close()
    a=classifier.predict(["imageToSave.png"], input_type='files')
    best_label=a[0]['label']
    (img1,img2,img3,url1,url2,url3) = someFunc(best_label)
    data = {}
    data["class"] = best_label
    data["items"] = [{"pic":img1,"url":url1},{"pic":img2,"url":url2},{"pic":img3,"url":url3}]
    data["percent"] = "100"
    
    for i in range(0,len(final)):
        if(array_final[i][1]==best_label):
            data["pic"] = final[i]
    
    return json.dumps(data)

if __name__ == "__main__":
    app.run(port=80)
    
def someFunc(best_label1):

  res=range(6)

  if(best_label1=="jim parson"):

      res[0]="https://www.zalando.de/tom-tailor-ray-hemd-navy-to222d07o-k11.html"

      res[1]="https://www.zalando.de/kiomi-the-casual-belt-guertel-cognac-k4452d002-708.html"

      res[2]="https://www.zalando.de/selected-homme-krawatte-navy-se622c00s-k12.html"

      res[3]="https://secure-i5.ztat.net//large/TO/22/2D/07/OK/11/TO222D07O-K11@13.jpg"

      res[4]="https://secure-i5.ztat.net//large/K4/45/2D/00/27/08/K4452D002-708@2.4.jpg"

      res[5]="https://secure-i4.ztat.net//large/SE/62/2C/00/SK/12/SE622C00S-K12@6.1.jpg"

  return res




    
