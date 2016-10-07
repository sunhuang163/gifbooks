# coding:utf-8

import pickle
from urllib.request import urlopen
from urllib.request import urlparse

from bs4 import BeautifulSoup


def get_links(urls, codec="utf-8", remark="id", flag=""):
    html = urlopen(urls).read()
    root_url = "http://" + urlparse(urls).netloc
    if remark is not 'id':
        links = BeautifulSoup(html, "html5lib", from_encoding=codec).find_all(class_=flag)
    else:
        links = BeautifulSoup(html, "html5lib", from_encoding=codec).find_all(id=flag)
    cs = []
    for link in links:
        try:
            href = root_url + link.find('a').attrs['href']
            title = link.find('a').get_text()
            cs.append({
                'href': href,
                'title': title})

        except:
            pass
    return cs


def get_article(url, codec="gb2312"):
    try:
        htmls = urlopen(url)
        bodys = BeautifulSoup(htmls, "html5lib", from_encoding=codec).find(class_='con').find("img")
        href = bodys.attrs['src']
        title = bodys.attrs['alt']
        return {
            'href': href,
            'title': title
        }
    except:
        return None


def get_all(startpage=1,end_page=2,codec="gb2312"):
    alls = []

    for i in range(startpage, end_page):
        if i == 1:
            urls = "http://www.gifcool.com/diaobao"
        else:
            urls = "http://www.gifcool.com/diaobao/list_4_%d.html" % i
        print("page=%d"%i)
        links = get_links(urls, codec, remark='class_', flag='title')
        for link in links:
            url = link['href']
            content = get_article(url)
            alls.append(content)
    pickle_file(str(end_page)+".txt",alls)
    return alls


def pickle_file(dest, contents):
    f = open(dest, 'wb')
    pickle.dump(contents, f)
    f.close()


def retive_file(source):
    f = open(source, 'rb')
    d = pickle.load(f)
    f.close()
    return d
# contents= get_all(startpage=120,end_page=121)


import threading,time,datetime
from time import sleep, ctime
def now() :
    return str( time.strftime( '%Y-%m-%d %H:%M:%S' , time.localtime() ) )
def main():
    print("start ",now())
    threadpool=[]
    start=1
    step=20
    end=86
    for i in range(start,end,step):
        th=[]
        print(i,i+step)
        th=threading.Thread(target=get_all,args=(i,i+step))
        threadpool.append(th)

    for thre in threadpool:
        thre.start()




if __name__ == '__main__':
        main()







