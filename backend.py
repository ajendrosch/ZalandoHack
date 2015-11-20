from metamind.api import ClassificationData, ClassificationModel, set_api_key
from flask import Flask, request
import json
from flask.ext.cors import CORS

set_api_key('sxXhflPZoxXz3USooJB9H2hD4frYjbJF83mZ6mZRscuVxasSuv')

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
    
def someFunc(best_label1):

    res=range(6)
    if(best_label1=="jim parson"):
        res[0]="https://www.zalando.de/tom-tailor-ray-hemd-navy-to222d07o-k11.html"
        res[1]="https://www.zalando.de/kiomi-the-casual-belt-guertel-cognac-k4452d002-708.html"
        res[2]="https://www.zalando.de/selected-homme-krawatte-navy-se622c00s-k12.html"
        res[3]="https://secure-i5.ztat.net//large/TO/22/2D/07/OK/11/TO222D07O-K11@13.jpg"
        res[4]="https://secure-i5.ztat.net//large/K4/45/2D/00/27/08/K4452D002-708@2.4.jpg"
        res[5]="https://secure-i4.ztat.net//large/SE/62/2C/00/SK/12/SE622C00S-K12@6.1.jpg"
    if(best_label1=="Anna Hathway"):
        res[0]="https://www.zalando.de/armani-jeans-jeans-slim-fit-black-aj121n008-q11.html"
        res[1]="https://www.zalando.de/evita-schnuerer-black-ev611c07n-q11.html"
        res[2]="https://www.zalando.de/anna-field-shopping-bag-black-an651ha0x-q11.html"
        res[3]="https://secure-i4.ztat.net//large/AJ/12/1N/00/8Q/11/AJ121N008-Q11@10.jpg"
        res[4]="https://secure-i6.ztat.net//large/EV/61/1C/07/NQ/11/EV611C07N-Q11@6.1.jpg"
        res[5]="https://secure-i4.ztat.net//large/AN/65/1H/A0/XQ/11/AN651HA0X-Q11@10.jpg"
    if(best_label1=="Taylor swift"):
        res[0]="https://www.zalando.de/vero-moda-cousin-bluse-black-ve121x00a-802.html"
        res[1]="https://www.zalando.de/reiss-brio-a-linien-rock-light-navy-claret-rb021b000-g11.html"
        res[2]="https://www.zalando.de/michael-michael-kors-jet-set-handtasche-vanilla-1mi51a00l-002.html"
        res[3]="https://secure-i1.ztat.net//large/VE/12/1X/00/A8/02/VE121X00A-802@1.3.jpg"
        res[4]="https://secure-i2.ztat.net//large/RB/02/1B/00/0G/11/RB021B000-G11@14.jpg"
        res[5]="https://secure-i3.ztat.net//large/1M/I5/1A/00/L0/02/1MI51A00L-002@1.1.jpg"
    if(best_label1=="David Schimmer"):
        res[0]="https://www.zalando.de/pepe-jeans-lederjacke-999black-pe122j02a-q11.html"
        res[1]="https://www.zalando.de/nike-sb-stefan-janoski-max-sneaker-ns412b00o-q11.html"
        res[2]="https://www.zalando.de/boss-orange-chino-dark-blue-bo122e00l-k13.html"
        res[3]="https://secure-i1.ztat.net//large/PE/12/2J/02/AQ/11/PE122J02A-Q11@18.1.jpg"
        res[4]="https://secure-i2.ztat.net//large/NS/41/2B/00/OQ/11/NS412B00O-Q11@18.jpg"
        res[5]="https://secure-i6.ztat.net//large/BO/12/2E/00/LK/13/BO122E00L-K13@14.jpg"
    if(best_label1=="michael jackson"):
        res[0]="https://www.zalando.de/calvin-klein-baker-sakko-claret-6ca22b005-g11.html"
        res[1]="https://www.zalando.de/selected-homme-sel-noos-krawatte-black-se652k000-q11.html"
        res[2]="https://www.zalando.de/versace-jeans-hemd-nero-1vj22d01a-q11.html"
        res[3]="https://secure-i6.ztat.net//large/6C/A2/2B/00/5G/11/6CA22B005-G11@16.jpg"
        res[4]="https://secure-i1.ztat.net//large/SE/65/2K/00/0Q/11/SE652K000-Q11@1.1.jpg"
        res[5]="https://secure-i3.ztat.net//large/1V/J2/2D/01/AQ/11/1VJ22D01A-Q11@2.jpg"
    if(best_label1=="Matthew Perry"):
        res[0]="https://www.zalando.de/globe-goodstock-chino-stone-gl522a00b-b11.html"
        res[1]="https://www.zalando.de/kiomi-wollmantel-klassischer-mantel-navy-k4422na08-k11.html"
        res[2]="https://www.zalando.de/g-star-2pack-t-shirt-basic-gs122o02t-q11.html"
        res[3]="https://secure-i4.ztat.net//large/GL/52/2A/00/BB/11/GL522A00B-B11@14.jpg"
        res[4]="https://secure-i3.ztat.net//large/K4/42/2N/A0/8K/11/K4422NA08-K11@20.jpg"
        res[5]="https://secure-i1.ztat.net//large/GS/12/2O/02/TQ/11/GS122O02T-Q11@6.jpg"
    if(best_label1=="david beckham"):
        res[0]="https://www.zalando.de/dickies-sacramento-hemd-di622f00m-m11.html"
        res[1]="https://www.zalando.de/bugatti-renato-business-schnuerer-cognac-bu112a06w-708.html"
        res[2]="https://www.zalando.de/501-jeans-01-le222b007-955.html"
        res[3]="https://secure-i2.ztat.net//large/DI/62/2F/00/MM/11/DI622F00M-M11@16.jpg"
        res[4]="https://secure-i5.ztat.net//large/BU/11/2A/06/W7/08/BU112A06W-708@26.jpg"
        res[5]="https://secure-i3.ztat.net//large/LE/22/2B/00/79/55/LE222B007-955@28.jpg"
    if(best_label1=="viktoria beckham"):
        res[0]="https://www.zalando.de/hugo-relini-a-linien-rock-offwhite-hu721b028-a11.html"
        res[1]="https://www.zalando.de/esprit-bluse-bordeaux-red-es121e07d-g11.html/"
        res[2]="https://www.zalando.de/buffalo-high-heel-pumps-patent-leather-cereza-bu311b032-g11.html"
        res[3]="https://secure-i4.ztat.net//large/ES/12/1E/07/DG/11/ES121E07D-G11@14.jpg"
        res[4]="https://secure-i4.ztat.net//large/HU/72/1B/02/8A/11/HU721B028-A11@14.jpg"
        res[5]="https://secure-i3.ztat.net//large/BU/31/1B/03/2G/11/BU311B032-G11@2.jpg"
    if(best_label1=="Jackie chan"):
        res[0]="https://www.zalando.de/your-turn-t-shirt-print-white-yo122oa0x-a11.html"
        res[1]="https://www.zalando.de/levi-s-the-trucker-jeansjacke-le222g00y-k12.html"
        res[2]="https://www.zalando.de/levi-s-511-jeans-blue-le222a01w-952.html"
        res[3]="https://secure-i6.ztat.net//large/YO/12/2O/A0/XA/11/YO122OA0X-A11@14.jpg"
        res[4]="https://secure-i2.ztat.net//large/LE/22/2G/00/YK/12/LE222G00Y-K12@16.jpg"
        res[5]="https://secure-i3.ztat.net//large/LE/22/2A/01/W9/52/LE222A01W-952@1.1.jpg"
    return res
    
@app.route("/upload", methods=['POST'])
def upload():
    img  = request.form['img']
    img = img.split(",")[1]
    fh = open("imageToSave.png", "wb")
    fh.write(img.decode('base64'))
    fh.close()
    a=classifier.predict(["imageToSave.png"], input_type='files')
    best_label=a[0]['label']
    [url1,url2,url3,img1,img2,img3] = someFunc(best_label)
    data = {}
    data["class"] = best_label
    data["items"] = [{"pic":img1,"url":url1},{"pic":img2,"url":url2},{"pic":img3,"url":url3}]
    data["percent"] = "100"
    
    for i in range(0,len(final)):
        if(final[i][1]==best_label):
            data["pic"] = final[i][0]
    
    return json.dumps(data)

if __name__ == "__main__":
    app.run(port=80,debug=True)
