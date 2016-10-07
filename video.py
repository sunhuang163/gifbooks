#coding:utf-8
import os,sys
path = os.getcwd()
sys.path.insert(0,path)
os.environ['DJANGO_SETTINGS_MODULE']="gifsite.settings"
import django
django.setup()
from mp4.models import Video,Sitelists
from utils.meipai import getmeipai
contents=getmeipai(startpage=120,endpage=320)
site=Sitelists.objects.first()
for cs in contents:
    for c in cs:
        try:
            Video.objects.create(site_name=site,video_url=c['video_url'],title=c['title'],img_url=c['img_url'])
            print("V")
        except:
            print("X")

