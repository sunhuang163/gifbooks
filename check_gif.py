# coding:utf-8
import os
import sys

path = os.getcwd()
sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = "gifsite.settings"
from PIL import Image
import django

django.setup()
from urllib.request import urlretrieve
from urllib import request
from joke.models import Articles
headers='Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1707.0 Safari/537.36'

imgs = Articles.objects.all()[3800:3999]
path ='tmp/'
dest='media/img/'
for img in imgs:
    id=img.id

    req = request.Request(img.fromlink)
    filename= request.urlparse(img.fromlink).path.split("/")[-1]
    req.add_header('User-Agent', headers)
    try:
        res=request.urlopen(req).read()
        with open(path+filename, 'wb') as f:
            f.write(res)
        im = Image.open(path+filename)
        im = im.resize((250, 156), Image.ANTIALIAS)
        im.save(dest+filename)
        os.remove(path+filename)
        img.snapshot="img/"+filename
        img.save()
        # Articles.objects.get(id=id).update(snapshot=+filename)
        # print("img/"+filename)
    except:
        pass

