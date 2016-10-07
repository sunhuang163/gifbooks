from django.shortcuts import render
from .models import Video,Sitelists
# Create your views here.
import os

def index(request):

    return render(request,template_name="index.html")

def lists(request):
    mp4_list= Video.objects.all()[:5]

    return render(request,template_name="lists.html",context={'mp4_lists':mp4_list})
