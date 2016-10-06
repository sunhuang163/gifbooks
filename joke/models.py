from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name='名称', unique=True)
    code = models.CharField(max_length=120, verbose_name='代码', unique=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name_plural = "分类"


class Sitelists(models.Model):
    name = models.CharField(max_length=120, verbose_name='抓取栏目名称')
    link = models.URLField(unique=True, verbose_name='链接地址')
    category = models.ForeignKey(Category, related_name='site_category', verbose_name='类型')
    utf8 = models.BooleanField(default=True, verbose_name='UTF-8编码')
    autofetch = models.BooleanField(default=True, verbose_name='自动抓取')
    disabled = models.BooleanField(default=False, verbose_name='关闭')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "抓取栏目"


class Tags(models.Model):
    name =models.CharField(max_length=20,unique=True,verbose_name='标识名称')
    isSearched = models.BooleanField(default=True)
    isDisabled =models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="TAG"

class Articles(models.Model):
    site = models.ForeignKey(Sitelists, related_name='article_sitelists', verbose_name='网站')
    title= models.CharField(max_length=120,verbose_name='标题')
    # tag = models.ForeignKey(Tags,null=True,blank=True,related_name='tag_articles')

    fromlink= models.CharField(max_length=200,verbose_name='来源',null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, blank=True)
    published =models.BooleanField(default=False)
    snapshot=models.ImageField(upload_to="img",null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together=('title','site','fromlink')
        verbose_name_plural="文章"

