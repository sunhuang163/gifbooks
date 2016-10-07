# coding:utf-8
from urllib.request import urlopen

from bs4 import BeautifulSoup

urls="http://www.meipai.com/square/13?single_column=1"

def get_meipai_gaoxiao(urls):
    try:
        htmls=urlopen(urls).read()
        conntents=BeautifulSoup(htmls,"html5lib",from_encoding="utf-8").find_all(class_="feed-item pr")
        data=[]
        for content in conntents:
            video_url=content.find(class_="feed-video pr cp").attrs['data-video']
            img_url=content.find("img").attrs['src']
            title=content.find("img").attrs['alt']
            data.append({
                'video_url':video_url,
                'title':title,
                'img_url':img_url
            })
        return data
    except:
        return None

def getmeipai(startpage=2,endpage=5):
    data=[]
    for i in range(startpage,endpage):
        urls = "http://www.meipai.com/square/13?single_column=1&p=%d"%i
        contents=get_meipai_gaoxiao(urls)
        data.append(contents)
    return data


