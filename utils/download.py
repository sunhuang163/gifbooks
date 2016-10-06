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


def get_all(end_page=2):
    alls = []
    for i in range(1, end_page):
        if i == 1:
            urls = "http://www.gifcool.com/meinv/"
        else:
            urls = "http://www.gifcool.com/meinv/list_2_%d.html" % i
        codec = "gb2312"
        links = get_links(urls, codec, remark='class_', flag='title')
        for link in links:
            url = link['href']
            content = get_article(url)
            alls.append(content)
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
# contents= get_all(68)
# pickle_file("dest.txt",contents)
# contents=retive_file("dest.txt")
# i=0
# for content in contents:
#     if content is None:
#         pass
#     else:
#         if len(content['titlet'])<2 :
#             pass
#         else:
#             netloc=urlparse(content['href']).netloc
#             if len(netloc)<10:
#                 i=i+1
#                 print("http://www.gifcool.com"+content['href'])
#
#
# print("total=%d"%i)
