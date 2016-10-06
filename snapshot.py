#coding:utf-8
from PIL import Image

import os

import os


def iterbrowse(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)


for fullname in iterbrowse("static/giflib"):
    dest=fullname.split("/")[-1].split("\\")[-1]
    img = Image.open(fullname)
    img = img.resize((250, 156), Image.ANTIALIAS)
    img.save("media/small/"+dest)
