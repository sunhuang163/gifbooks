from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.
class SiteLists(models.Model):
    name = models.CharField(max_length=120, verbose_name="小说网站")
    search_page = models.URLField(unique=True, verbose_name="入口")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    codec = models.CharField(max_length=120, verbose_name="编码格式", default='GB2312')
    online=models.BooleanField(default=True,verbose_name="是否在线")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "小说网站"


class Novel(models.Model):
    name = models.CharField(max_length=120, verbose_name='书名')
    from_site = models.ForeignKey(SiteLists, related_name="novel_site", verbose_name="来自")
    author = models.CharField(max_length=120, verbose_name='作者', default="来自网络")
    completed = models.BooleanField(default=False, verbose_name='是否完本')
    links = models.URLField(unique=True, verbose_name='小说目录地址')
    isSuccess = models.BooleanField(default=False, verbose_name="是否有效")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    category = models.CharField(max_length=120, verbose_name="类别")
    published = models.BooleanField(default=True, verbose_name="是否发布")

    def __str__(self):
        return self.name + "_" + self.author

    class Meta():
        verbose_name_plural = "小说名称"


class Article(models.Model):
    novel = models.ForeignKey(Novel, related_name='novel_article')
    title = models.CharField(max_length=250,verbose_name="章节名")
    links= models.URLField(unique=True,verbose_name="链接地址")
    content= RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    published = models.BooleanField(default=True,verbose_name="是否发布")

    def __str__(self):
        return self.novel.name+"__"+self.title

    class Meta():
        verbose_name_plural="小说内容"


