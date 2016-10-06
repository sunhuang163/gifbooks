from django.contrib import admin
from .models import Category,Articles,Tags,Sitelists
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ('site','title','preview','fromlink')
    list_filter = ('site','created_date')
    date_hierarchy = 'created_date'
    search_fields = ('title',)
    def preview(self, obj):
        if ".gif" in obj.fromlink:
            return '<img src="%s" height="80" width="128" />' % (obj.fromlink)
        else:
            return None
    preview.allow_tags = True
    preview.short_description = "图片"

class SiteListsAdmin(admin.ModelAdmin):
    list_display = ('category','name','link','utf8','created_date')

admin.site.register(Category)
admin.site.register(Articles,ArticleAdmin)
admin.site.register(Tags)
admin.site.register(Sitelists,SiteListsAdmin)
