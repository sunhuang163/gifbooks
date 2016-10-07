from django.contrib import admin
from .models import Sitelists,Video
# from reversion.admin import VersionAdmin
# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title','preview','preview1')
    list_per_page = 5
    def preview(self, obj):
        if ".mp4" in obj.video_url:
            return '<video src="%s" width="160" height="220" controls stop loop> <source type=video/mp4 />Your browser does not support the video tag.</video> ' % (obj.video_url)
        else:
            return None
    preview.allow_tags = True
    preview.short_description = "视频"
    def preview1(self, obj):
        if ".mp4" in obj.video_url:
            return '<img src="%s" height="220" width="160" />  ' % (obj.img_url)
        else:
            return None
    preview1.allow_tags = True
    preview1.short_description = "快照"

admin.site.register(Video,VideoAdmin)
admin.site.register(Sitelists)
