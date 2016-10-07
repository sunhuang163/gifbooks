#coding:utf-8
import os,sys
path = os.getcwd()
sys.path.insert(0,path)
os.environ['DJANGO_SETTINGS_MODULE']="gifsite.settings"
import django
django.setup()
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

from novels.models import SiteLists,Article,Novel



def get_book_home_list(start_urls=""):
    try:
        body = urlopen(start_urls).read()
        html = BeautifulSoup(body, "html5lib", from_encoding="gbk").find(class_="clearfix rec_rullist").find_all("ul")
        lastpage = BeautifulSoup(body, "html5lib", from_encoding="gbk").find(class_="last").get_text()
        content = []
        for uls in html:
            link = uls.find(class_="two").find("a").attrs['href']
            title = str.replace(uls.find(class_="two").find("a").get_text(), "全文阅读", "")
            author = str.replace(uls.find(class_="four").find("a").get_text(), "全本", "")
            updated_date = uls.find(class_="six").get_text()

            category = uls.find(class_="sev").get_text()
            content.append(
                {
                    'title': title,
                    'link': link,
                    'category': category,
                    'author': author,
                    'update_date': updated_date,
                    'total': lastpage
                })
        return {'lastpage':lastpage,'content':content}
    except:
        return None


# print(get_update_list(start_urls))
# article_links="http://www.ybdu.com/xiaoshuo/13/13774/"
# link="6592950.html"
# a_links=article_links+link
def get_content(a_link=""):
    none_div=re.compile('<[^>]+>')
    body=urlopen(a_link).read()

    html = BeautifulSoup(body, "html5lib", from_encoding="gbk").find(id="htmlContent").prettify()
    title = BeautifulSoup(body, "html5lib", from_encoding="gbk").find(class_="h1title").find("h1").get_text()
    con=none_div.sub("",html)
    return con

# get_content(a_link=a_links)




def get_article_links(article_links=""):
    try:
        body=urlopen(article_links).read()
        html=BeautifulSoup(body,"html5lib",from_encoding="gbk").find(class_="mulu_list").find_all("li")
        content=[]
        for lis in html:
            title=lis.get_text()
            link=lis.find("a").attrs['href']
            content.append({
                'title':title,
                'link':link
            })
        return content

    except:
        return None


if __name__ == "__main__":
    # site = SiteLists.objects.first()
    # start_urls = site.search_page%1
    # total=int(get_book_home_list(start_urls=start_urls)['lastpage'])
    # print("%d"%total)
    # for i in range(5,50):
    #     url=site.search_page%i
    #     lists=get_book_home_list(url)
    #     books=lists['content']
    #     for book in books:
    #         try:
    #             novel=Novel.objects.create(
    #                 name=book['title'],
    #                 from_site=site,
    #                 author=book['author'],
    #                 links=book['link'],
    #                 category=book['category']
    #             )
    #             print(book)
    #         except:
    #             print("existed")

   #  读取Novel 表获取文章内容
    novels= Novel.objects.all()[:2]
    for n in novels:
        article_start_link=n.links
        article_links=get_article_links(article_links=article_start_link)
        for article_link in article_links:

            a_link=article_start_link+article_link['link']
            try:
                c = get_content(a_link)
                Article.objects.create(
                    novel=n,
                    title=article_link['title'],
                    links=a_link,
                    content=c)
                print('pass')
            except:
                print("X")


