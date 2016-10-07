"""gifsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from joke.models import Articles
from mp4.models import Video

DIRNAME = os.path.dirname(__file__)
from django.conf.urls.static import static

from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('video_url', 'title', 'img_url')


# ViewSets define the view behavior.
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)


# Article API
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articles
        fields = ('id', 'title', 'fromlink', 'snapshot')


# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer


ArticleRouter = routers.DefaultRouter()
ArticleRouter.register(r'article', ArticleViewSet)
info_dict = {
    'queryset': Video.objects.all(),
    'date_field': 'created_date',
}

urlpatterns = [
                  url(r'^', include(router.urls)),
                  url(r'^api/', include(ArticleRouter.urls)),
                  
                  url(r'^mp4/', include("mp4.urls"), name="mp4"),
                 
                  url(r'^admin/', admin.site.urls),

                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^ckeditor/', include('ckeditor_uploader.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
