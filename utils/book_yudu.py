start_urls = "http://www.ybdu.com/book/lastupdate/0/1/"
from urllib.request import urlopen

from bs4 import BeautifulSoup
import re





def get_update_list(start_urls=""):
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
article_links="http://www.ybdu.com/xiaoshuo/13/13774/"
link="6592950.html"
a_links=article_links+link
def get_content(a_link=""):
    none_div=re.compile('<[^>]+>')
    body=urlopen(a_link).read()

    html = BeautifulSoup(body, "html5lib", from_encoding="gbk").find(id="htmlContent").prettify()
    title = BeautifulSoup(body, "html5lib", from_encoding="gbk").find(class_="h1title").find("h1").get_text()
    con=none_div.sub("",html)
    print(title,a_link)

get_content(a_link=a_links)




def get_article_links(article_links=""):
    try:
        body=urlopen(article_links).read()
        html=BeautifulSoup(body,"html5lib",from_encoding="gbk").find(class_="mulu_list").find_all("li")
        for lis in html:
            title=lis.get_text()
            link=lis.find("a").attrs['href']
            print(link)
    except:
        return None