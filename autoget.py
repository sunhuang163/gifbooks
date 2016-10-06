#coding:utf-8
import os,sys
path = os.getcwd()
sys.path.insert(0,path)
os.environ['DJANGO_SETTINGS_MODULE']="gifsite.settings"
import django
django.setup()

from joke.models import Articles,Sitelists,Tags
from urllib.request import urlparse
from utils.download import get_all,pickle_file,retive_file
def get_gifcool(startpage=2,filename="gifcool,txt",sitename=""):
    contents= get_all(startpage)
    pickle_file(filename,contents)
    contents=retive_file(filename)
    for content in contents:
        if content is None:
            pass
        else:
            if len(content['title'])<2 :
                pass
            else:
                netloc=urlparse(content['href']).netloc
                if len(netloc)<10:
                    content['href']="http://www.gifcool.com"+content['href']
                try:
                    Articles.objects.create(site=sitename,title=content['title'],fromlink=content['href'],content=content['href'])
                    print('ok')
                except:
                    pass




sites=Sitelists.objects.all()
for site in sites:
    if site.link == "http://www.gifcool.com/meinv":
        print("start download %s - %s" % (site.name, site.link))
        #get_gifcool(startpage=68, filename="gifcool,txt", sitename=site)
    elif site.link=='http://www.gifcool.com/fun':
        try:
            Tags.objects.create(name="搞笑动画")
        except:
            pass
            # contents=retive_file('utils/160.txt')
            # for content in contents:
            #     if content is not None:
            #
            #         netloc = urlparse(content['href']).netloc
            #         if len(netloc) < 10:
            #             content['href'] = "http://www.gifcool.com" + content['href']
            #         try:
            #             Articles.objects.create(site=site, title=content['title'], fromlink=content['href'],
            #                                     content=content['href'])
            #             print('ok')
            #         except:
            #             pass
    elif site.link=='http://www.gifcool.com/diaobao':
        contents=retive_file('utils/81.txt')
        for content in contents:
            if content is not None:
                netloc = urlparse(content['href']).netloc
                if len(netloc) < 10:
                    content['href'] = "http://www.gifcool.com" + content['href']
                try:
                    Articles.objects.create(site=site, title=content['title'], fromlink=content['href'],
                                            content=content['href'])
                    print('==')
                except:
                    pass


