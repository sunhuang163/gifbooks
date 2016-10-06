from django.db import models

# Create your models here.

class Novel(models.Model):
    name   = models.CharField(max_length=120,verbose_name='书名')
    author = models.CharField(max_length=120,verbose_name='作者',default="来自网络")
    completed = models.BooleanField(default=False,verbose_name='是否完本')

    from_to=models.URLField(unique=True) #小说来源网站

    def __str__(self):
        return self.name+"_"+self.author

class Article(models.Model):

    novel=models.ForeignKey(Novel,related_name='novel_article')
