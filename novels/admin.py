from django.contrib import admin

from .models import SiteLists, Article, Novel


# Register your models here.
class SiteListsAdmin(admin.ModelAdmin):
    list_display =  ('name', 'search_page', 'updated_date', 'codec','online')

class NovelAdmin(admin.ModelAdmin):
    list_display = ('from_site','preview','author','category')
    list_filter = ('from_site','category')
    list_per_page = 20
    search_fields = ('author','name')

    def preview(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (obj.links,obj.name)
    preview.allow_tags = True
    preview.short_description = "链接"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','novel','title','links')
    list_per_page = 20


admin.site.register(SiteLists, SiteListsAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Novel,NovelAdmin)
