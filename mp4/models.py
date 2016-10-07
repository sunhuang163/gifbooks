from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Sitelists(models.Model):
    name = models.CharField(max_length=120, verbose_name='Mp4网站名称')
    link = models.URLField(unique=True, verbose_name='链接地址')
    utf8 = models.BooleanField(default=True, verbose_name='UTF-8编码')
    autofetch = models.BooleanField(default=True, verbose_name='自动抓取')
    disabled = models.BooleanField(default=False, verbose_name='关闭')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='更新时间', null=True, blank=True)
    content = RichTextUploadingField(null=True,config_name='basic')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "网站"
class Video(models.Model):
    site_name=models.ForeignKey(Sitelists,related_name="Site")
    title=models.CharField(max_length=250,verbose_name="Title")
    video_url=models.URLField(verbose_name="视频网址")
    img_url= RichTextField(verbose_name="快照网址")
    created_date =models.DateTimeField(auto_now_add=True)
    published=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class Meta:
        unique_together=('site_name','title','video_url')
        verbose_name_plural="视频列表"




