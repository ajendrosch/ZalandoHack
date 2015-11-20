from metamind.api import ClassificationData, ClassificationModel, set_api_key
from flask import Flask, request
import json
from flask.ext.cors import CORS

set_api_key('nDdCYFXwkFPp8b0O2L7aQRmY7aOfdnOtSodaHP3rA9eIKXqhqe')

classifier = ClassificationModel(id='40301')

#################################### MALE
david=[
       'http://assets.esquire.co.uk/images/uploads/fourbythree/_1080_43/David-Beckham-H-and-M-hair-43.jpg',
       'http://i.dailymail.co.uk/i/pix/2015/02/08/257B2FFC00000578-0-image-m-2_1423432943337.jpg',
       'http://blog.colourfulrebel.com/en/wp-content/uploads/2015/09/David-Beckham-Bodywear-3.jpg',
       'http://www.iradio.ie/blog/wp-content/uploads/2015/07/david-beckham.jpg',
       'http://blog.e-shot.net/blog/wp-content/uploads/2015/09/david_beckham-759.jpg',
       'http://images.ok.co.uk/1428678736_david-beckham-godfather-liv-tyler-son.jpg',
       'http://specials-images.forbesimg.com/imageserve/0248f817595741bca8b685fa1aa816e5/320x486.jpg',
       'http://media1.popsugar-assets.com/files/2015/03/20/719/n/2589278/da1b3b88_edit_img_cover_file_401219_1426867564_davidvc9eUh.xxxlarge/i/Most-Gorgeous-Photos-David-Beckham.jpg',
       'https://voolas.com/wp-content/uploads/2015/08/305970-david-beckham.jpg',
       'http://images.huffingtonpost.com/2015-01-31-DavidBeckhamToaststheArrivalofHaigClubSingleGrainScotchWhiskytotheUSinLA_PhotoCreditTomBunning.jpg'
       ]
ray=['http://kalamu.com/neogriot/wp-content/uploads/2014/03/ray-charles-01.jpg',
     'http://blogcritics.org/wp-content/uploads/bcimages/2013/09/ray-charles-forever.png',
     'https://fanart.tv/fanart/music/2ce02909-598b-44ef-a456-151ba0a3bd70/artistbackground/ray-charles-4e518cac06917.jpg',
     'http://orig08.deviantart.net/3223/f/2012/264/b/4/b4e86ad03fd7354c424de1ae689358a5-d5fg420.jpg',
     'http://4.bp.blogspot.com/-2kaasii3SSU/TllqRd3HUsI/AAAAAAAAKZg/uiGJGMRG_1g/s1600/Portrait+-+poss+Russia%252C+Ray+Charles+-+late+1990s.jpg',
     'http://image.slidesharecdn.com/raycharles2-141122123115-conversion-gate01/95/ray-charles-1966-26-638.jpg?cb=1416659550',
     'http://www.rockpaperphoto.com/media/catalog/product/cache/1/small_image/17f82f742ffe127f42dca9de82fb58b1/1/7/1778_2.jpg',
     'http://i.ytimg.com/vi/fRgWBN8yt_E/0.jpg',
     'https://irom.files.wordpress.com/2011/10/ray-charles-1974.jpg']
eminem=['http://coolspotters.com/files/photos/506009/eminem-profile.jpg?1357458187',
        'https://s-media-cache-ak0.pinimg.com/236x/b6/18/f5/b618f5f34688846ee07e17c420d9145b.jpg',
        'http://images.fashionnstyle.com/data/images/full/53098/109065485-jpg.jpg',
        'http://img2.bdbphotos.com/images/orig/a/c/acctzurhfb6ee6h.jpg?skj2io4l',
        'http://www.hdrpainting.com/wp-content/uploads/2011/02/Eminem_01.jpg',
        'https://metrouk2.files.wordpress.com/2014/03/wpid-article-1314803627189-0d85d1b300000578-256459_636x540.jpg',
        'http://www.timsackett.com/wp-content/uploads/2012/04/eminem-e1335359826524.jpg',
        'http://images.fashionnstyle.com/data/images/full/53111/1418095-jpg.jpg',
        'http://i00.i.aliimg.com/wsphoto/v0/1692267632/Onsale-28-44-baggy-jeans-men-black-hiphop-jeans-for-men-rapper-style-eminem-pant-plus.jpg'
        ]
#################################### FEMALE
jennifer=[
          'http://a3.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE4MDAzNDEwNzQ4NjA1OTY2.jpg',
          'http://www.trbimg.com/img-55b6c486/turbine/la-et-jennifer-lopez-birthday-dress-casper-smart-20150727/1050/1050x591',
          'https://upload.wikimedia.org/wikipedia/commons/c/c3/Jennifer_Lopez_at_GLAAD_Media_Awards.jpg',
          'http://i1.mirror.co.uk/incoming/article6143571.ece/ALTERNATES/s1227b/Jennifer-Lopez.jpg',
          'http://i.huffpost.com/gen/2961010/thumbs/o-JENNIFER-LOPEZ-900.jpg?6',
          'http://images1.mtv.com/uri/mgid:uma:video:mtv.com:742096?width=657&height=370&crop=true&quality=0.85'
          ]
aniston=[
         'http://a4.files.biography.com/image/upload/c_fill,cs_srgb,dpr_1.0,g_face,h_300,q_80,w_300/MTE4MDAzNDEwNDM1NzM3MTAy.jpg',
         'http://data.whicdn.com/images/61079654/original.jpg',
         'https://upload.wikimedia.org/wikipedia/commons/a/ac/JenniferAniston08TIFF.jpg',
         'http://i.huffpost.com/gen/2241868/images/o-JENNIFER-ANISTON-facebook.jpg'
         ]

edit=['http://blog.parisattitude.com/wp-content/uploads/2014/12/edith-piaf32933.jpg',
      'https://maggiemcneill.files.wordpress.com/2011/12/edith-piaf.jpg',
      'http://www.mtv.com/crop-images/2013/08/20/Edith%20Piaf%201950%20Gaston%20Paris.jpg',
      'http://en.parisinfo.com/var/otcp/sites/images/media/1.-photos/02.-sites-culturels-630-x-405/vertical-sites-culturels-405x630/musee-edith-piaf-portrait-noir-et-blanc-autographe-405x630-c-dr/138396-1-fre-FR/Musee-Edith-Piaf-portrait-noir-et-blanc-autographe-405x630-C-DR_block_media_big.jpg',
      'https://charlespaolino.files.wordpress.com/2011/05/edith-piaf-3.jpg',
      'http://lucastheatre.com/wp-content/uploads/2014/05/edith.jpg',
      'http://s3.amazonaws.com/quietus_production/images/articles/13829/edith_piaf_1384345410_crop_550x310.jpg',
      'http://i.telegraph.co.uk/multimedia/archive/02700/Edith-Piaf_2700431k.jpg',
      'http://hdwallx.com/wp-content/uploads/2014/07/Frances-greatest-international-stars-4-edith-piaf.jpg']
kylie=['http://de.eonline.com/eol_images/Entire_Site/2015717/rs_600x600-150817094651-600.Kylie-Jenner-Lip-Line.jl.081715.jpg',
       'http://img2.timeinc.net/people/i/2015/news/150504/kylie-jenner-768.jpg',
       'http://de.eonline.com/eol_images/Entire_Site/2015624/rs_600x600-150724100353-600.3.Kylie-Jenner-Graduation-Instagram.jl.072415.jpg',
       'https://cdn.shopify.com/s/files/1/0143/4652/t/6/assets/Kylie-img-1.png?35242',
       'https://res.cloudinary.com/galore/image/upload/c_scale,h_1600,q_100/v1441655241/Kylie_Jenner_Galore_Mag_12.jpg',
       'http://www.gannett-cdn.com/-mm-/66461ee078ab0133ded788e0f990968b9c16df3a/c=0-0-3914-2211&r=x1683&c=3200x1680/local/-/media/2015/04/21/USATODAY/USATODAY/635652004461329546-KYLIE-JENNER.JPG',
       'http://images.enstarz.com/data/images/full/73271/kylie-jenner.jpg?w=580',
       'http://cosmouk.cdnds.net/15/21/1600x800/landscape_nrm_1431950079-kylie-jenner.jpg',
       'http://i2.mirror.co.uk/incoming/article6270294.ece/ALTERNATES/s615b/Kylie-Jenner-on-Instagram.jpg',
       'http://media2.popsugar-assets.com/files/2014/11/24/799/n/1922153/43f19f5e3fbd21c2_thumb_temp_cover_file157414991416850382uyENLi.xxxlarge/i/Kylie-Jenner-Makeup-2014-American-Music-Awards.jpg',
       'http://www.efashiongossips.com/wp-content/uploads/2015/10/Kylie-Jenner_glamour.jpg',
       'https://s-media-cache-ak0.pinimg.com/236x/96/12/10/96121075a404f7941978b917c9953d6d.jpg',
       'https://s-media-cache-ak0.pinimg.com/236x/3c/2f/e3/3c2fe3debaddaaf1885ef89e88359d56.jpg',
       'https://s-media-cache-ak0.pinimg.com/236x/ff/cc/6f/ffcc6f16e55c1498865f09337124c4b8.jpg',
       'http://newfashioncraze.com/wp-content/uploads/2015/10/kylie-jenner.jpg',
       'http://celebmafia.com/wp-content/uploads/2015/02/kylie-jenner-style-at-sugarfish-sushi-in-calabasas-feb.-2015_7.jpg',
       'http://www.scotcampus.com/wp-content/uploads/2015/03/dujour-magazines-jason-binn-celebrates-kendall-and-kylie-jen-1.jpg',
       'http://stealherstyle.net/wp-content/uploads/2013/01/kylie-jenner-outfit-5.jpg',
       'https://s-media-cache-ak0.pinimg.com/236x/6d/14/ef/6d14ef16630c1e063b9c81b5b4d44bed.jpg',
       'http://i.dailymail.co.uk/i/pix/2015/03/30/12/2721C7E400000578-0-image-a-76_1427713292321.jpg',
       'http://static1.squarespace.com/static/53ab681fe4b0927a7cdfd8ba/53bc0ceae4b054e2f4ed92be/53bc0bebe4b017640b277890/1404832756060/Kendall-and-Kylie-Tumblr-Tuesday-Kylie-Jenner-Fashion-Style-Photos-32.png',
       'http://www.thelifestylereporter.com/wp-content/uploads/2015/02/Kylie-Jenner-Oversized-Denim-Shirt.jpg',
       'https://thefashiontag.files.wordpress.com/2014/06/kylie-jenner-style-2.jpg',
       'http://assets.elleuk.com/gallery/25033/2015-03-01-kylie-jenner-out-and-about-in-la-rex__large.jpg',
       'http://cdni.condenast.co.uk/320x480/k_n/Kylie-Jenner-June-2014-Vogue-12Aug14%20Rex_b_320x480.jpg',
       'http://static1.squarespace.com/static/53ab681fe4b0927a7cdfd8ba/53bc0ceae4b054e2f4ed92be/54d16497e4b0d39db788c74f/1423008920434/1000w.png',
       'http://celebmafia.com/wp-content/uploads/2015/04/kylie-jenner-style-out-in-los-angeles-march-2015_3.jpg',
       'https://s-media-cache-ak0.pinimg.com/736x/62/2f/1f/622f1fa0a9fee77440863c194761aefc.jpg'
       ]
array1=[
        ('http://a3.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE4MDAzNDEwNzQ4NjA1OTY2.jpg', 'Jennifer'),
        ('http://www.trbimg.com/img-55b6c486/turbine/la-et-jennifer-lopez-birthday-dress-casper-smart-20150727/1050/1050x591', 'Jennifer'),
        ('https://upload.wikimedia.org/wikipedia/commons/c/c3/Jennifer_Lopez_at_GLAAD_Media_Awards.jpg', 'Jennifer'),
        ('http://images1.mtv.com/uri/mgid:uma:video:mtv.com:742096?width=657&height=370&crop=true&quality=0.85','Jennifer'),
        ('http://www.olisa.tv/wp-content/uploads/2015/09/jennifer.jpg','Jennifer'),
        
        ('http://a4.files.biography.com/image/upload/c_fill,cs_srgb,dpr_1.0,g_face,h_300,q_80,w_300/MTE4MDAzNDEwNDM1NzM3MTAy.jpg', 'Aniston'),
        ('http://data.whicdn.com/images/61079654/original.jpg', 'Aniston'),
        ('https://upload.wikimedia.org/wikipedia/commons/a/ac/JenniferAniston08TIFF.jpg', 'Aniston'),
        ('http://i.huffpost.com/gen/2241868/images/o-JENNIFER-ANISTON-facebook.jpg', 'Aniston'),
        ('http://photos.laineygossip.com/articles/jennifer-aniston-sag-26jan15-04.jpg', 'Aniston'),
        ('http://photos.laineygossip.com/articles/aniston-cake-review-15sept14.jpg', 'Aniston'),
        
        ('https://news.artnet.com/wp-content/news-upload/2015/08/Brad_Pitt_Fury_2014-e1440597554269.jpg', 'Brad pitt'),
        ('http://media4.popsugar-assets.com/files/2014/04/12/866/n/1922398/38103bc2fe1cf5f3_116433PCN_BradGallery03_wm.xxxlarge/i/Brad-Pitt-Gets-Parking-Ticket-Pictures.jpg', 'Brad pitt'),
        ('http://cdn-img.people.com/emstag/i/2008/stylewatch/gallery/airport_styleadds/081222/brad_pitt200.jpg', 'Brad pitt'),
        ('http://i.dailymail.co.uk/i/pix/2013/03/09/article-0-1889DAB7000005DC-119_634x929.jpg', 'Brad pitt'),
        ('http://gq.co.za/wp-content/uploads/2015/01/rs_634x1024-150104083158-634.Brad-Pitt-Palm-Springs.jl_.010415.jpg', 'Brad pitt'),
        ('https://s-media-cache-ak0.pinimg.com/736x/4e/e9/2f/4ee92f814e8870ce6c048cb3dd242ba0.jpg', 'Brad pitt'),
        
        ('http://a3.files.biography.com/image/upload/c_fit,cs_srgb,dpr_1.0,h_1200,q_80,w_1200/MTE1ODA0OTcxMjkwNTYwMDEz.jpg', 'michael jackson'),
        ('http://www.figures.com/forums/attachment.php?attachmentid=8939&d=1279119533', 'michael jackson'),
        ('http://www.mensflair.com/media/michael-jackson-style.jpg', 'michael jackson'),
        ('http://2.bp.blogspot.com/_YZMZdWCxTvY/SkQh4rfNd4I/AAAAAAAAEFA/8A_u0rDbkGg/s400/michael+jackson2.jpg', 'michael jackson'),
        ('http://images2.fanpop.com/image/photos/10300000/MICHAEL-JACKSON-michael-jackson-10317030-1082-1263.jpg', 'michael jackson'),
        
        ('http://i.dailymail.co.uk/i/pix/2012/02/15/article-2101315-11BD4037000005DC-23_224x423.jpg', 'khan'),
        ('http://i969.photobucket.com/albums/ae180/shahrukhkhanonly2010-2/SRK%20photo%20shooting%20pics/n-16-Shahrukh-khan.jpg', 'khan'),
        ('http://i969.photobucket.com/albums/ae180/shahrukhkhanonly2010-2/SRK%20photo%20shooting%20pics/Shahrukh-khan-2.jpg~original', 'khan'),
        ('https://s-media-cache-ak0.pinimg.com/236x/05/62/e6/0562e612fcdcde8810dafba9ef73888e.jpg', 'khan'),
        
        ('http://photos.laineygossip.com/articles/taylor-swift-15jan15-05.jpg', 'Taylor swift'),
        ('http://de.eonline.com/eol_images/Entire_Site/2014312/rs_634x1024-140412172759-634.Taylor-Swift-jmd-041214_copy.jpg', 'Taylor swift'),
        ('http://celebmafia.com/wp-content/uploads/2014/11/taylor-swift-style-leaving-returning-to-her-apartment-in-new-york-city-november-2014_6.jpg', 'Taylor swift'),
        ('http://celebmafia.com/wp-content/uploads/2015/06/taylor-swift-style-at-lax-airport-june-2015_5.jpg', 'Taylor swift'),
        ('http://cdn1-www.thefashionspot.com/assets/uploads/gallery/taylor-swift-style-evolution/taylor-swift-crop-top.jpg', 'Taylor swift'),
        ('http://cosmouk.cdnds.net/cm/14/30/53d3251461c43_-_061212-taylor-swift-grammy-nominees-lgn.jpg', 'Taylor swift'),
        
        
        
        
        
        
        ('http://www4.pictures.stylebistro.com/bg/Courteney+Cox+Jeans+Skinny+Jeans+8n4Z6-Re49Cl.jpg', 'Courteney Cox'),
        ('http://cdni.condenast.co.uk/592x888/a_c/ccoc_gl_15apr11_rex_592x888.jpg', 'Courteney Cox'),
        ('http://celebmafia.com/wp-content/uploads/2014/11/courteney-cox-street-style-out-in-beverly-hills-november-2014_4.jpg', 'Courteney Cox'),
        ('http://cdni.condenast.co.uk/592x888/a_c/ccox_gl_18oct11_pa.jpg', 'Courteney Cox'),
        ('http://img2.timeinc.net/people/i/2008/stylewatch/hitormiss/080310/courteney_cox2.jpg', 'Courteney Cox'),
        ('http://cdn02.cdn.justjared.com/wp-content/uploads/2012/11/cox-halloween/courteney-cox-coco-halloween-shopping-fun-05.jpg', 'Courteney Cox'),
        ('http://i.dailymail.co.uk/i/pix/2015/07/08/03/2A513F1C00000578-3152997-Business_chic_Courteney_Cox_51_donned_a_street_chic_style_on_Tue-m-59_1436322572188.jpg', 'Courteney Cox'),
        ('http://cdn02.cdn.justjared.com/wp-content/uploads/2012/11/cox-halloween/courteney-cox-coco-halloween-shopping-fun-05.jpg', 'Courteney Cox'),
        ('http://www.fabzz.com/wp-content/uploads/celebs/2015/06/10/courteney-cox-style-out-in-beverly-hills/courteney-cox-style-out-in-beverly-hills-04-320x440.jpg', 'Courteney Cox'),
        
        ('http://static.entertainmentwise.com/images/5498a6067b388.jpg', 'David Schimmer'),
        ('https://s3.yimg.com/bt/api/res/1.2/itZ8qZjRdCz_jrvMDouWIQ--/YXBwaWQ9eW5ld3NfbGVnbztxPTg1O3NtPTE7dz0zMTA-/http://l.yimg.com/os/publish-images/omg/2014-05-27/17448b30-e596-11e3-b558-fb6ff763cb66_DavidSchwimmer_052714.jpg', 'David Schimmer'),
        ('http://i.dailymail.co.uk/i/pix/2015/05/12/16/2892A11600000578-0-image-m-10_1431445560818.jpg', 'David Schimmer'),
        ('https://s-media-cache-ak0.pinimg.com/236x/d8/a6/f2/d8a6f2f9fea0cd5388bd69eca2df84f9.jpg', 'David Schimmer'),
        ('http://planetecinema.free.fr/images%20celeb%20friends/david2.jpg', 'David Schimmer'),
        ('http://www.contactmusic.com/pics/lf/CFF_cannes_celebs_180512/david-schwimmer-during-the-65th-cannes-film_3888430.jpg', 'David Schimmer'),
        
        
        ('https://s-media-cache-ak0.pinimg.com/236x/6c/59/4b/6c594b12af3e0aca0f56282c906b9893.jpg', 'Matthew Perry'),
        ('http://gifrific.com/wp-content/uploads/2013/03/Chandler-Laughing-to-Himself-320x320.gif', 'Matthew Perry'),
        ('http://ak-hdl.buzzfed.com/static/enhanced/webdr01/2013/2/14/14/enhanced-buzz-21231-1360868865-6.jpg','Matthew Perry'),
        ('http://cdn.images.express.co.uk/img/dynamic/79/590x/secondary/Matthew-Perry-262818.jpg', 'Matthew Perry'),
        ('https://s-media-cache-ak0.pinimg.com/236x/c9/ae/cf/c9aecf1e639a06d8277a587f280882ee.jpg', 'Matthew Perry'),
        ('http://64.13.254.173/imgs/m2.jpg', 'Matthew Perry'),
        
        ('http://celebritiestown.com/celebritypictures/var/albums/Anne-Hathaway-style-Brooklyn/anne-hathaway-style-02.jpg', 'Anna Hathway'),
        ('http://i.dailymail.co.uk/i/pix/2014/09/04/article-2744260-210E97E600000578-605_634x849.jpg', 'Anna Hathway'),
        ('http://rentfrockrepeat.com/site/wp-content/uploads/2014/11/Anne-Hathaway-Vogue-27Oct14-Rex_b_592x888.jpg', 'Anna Hathway'),
        ('http://www.becauseiamfabulous.com/wp-content/uploads/2012/09/Anne-Hathaway-Married-Wedding-Dress-Husband-Style-wearing-black-dolce-gabbana-dress.jpg', 'Anna Hathway'),
        ('https://kniftonholdingcourt.files.wordpress.com/2012/08/anne-hathaway-tdkr-style.jpg', 'Anna Hathway'),
        ('http://www.femminastyle.com/wp-content/uploads/2013/02/anne-hathaway-the-devil-wears-prada-3-januari.jpeg', 'Anna Hathway')
        ]

array=range(len(david)+len(jennifer)+len(aniston)+len(ray)+len(edit)+len(kylie))
c=0
for i in range(0,len(david)):
    array[c]=(david[i],'david')
    c=c+1
for i in range(0,len(jennifer)):
    array[c]=(jennifer[i], 'Jennifer')
    c=c+1
for i in range(0,len(aniston)):
    array[c]=(aniston[i], 'Aniston')
    c=c+1
for i in range(0,len(ray)):
    array[c]=(ray[i], 'ray')
    c=c+1
for i in range(0,len(edit)):
    array[c]=(edit[i], 'edit')
    c=c+1
for i in range(0,len(kylie)):
    array[c]=(kylie[i], 'kylie')
    c=c+1

array_final=array+array1

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
    data = {}
    for i in range(0,len(array_final)):
        if(array_final[i][1]==best_label):
            data["result"] = array_final[i][0]
    
    return json.dumps(data)

if __name__ == "__main__":
    app.run(port=80)




    
