#!/usr/local/bin/python3
#coding=utf-8

import os, io, sys, re, time, json, random
from PIL import Image, ImageEnhance, ImageFilter

def watermark(img_source, img_water, img_new, offset_x, offset_y):
    try:
        im = Image.open(img_source)
        wm = Image.open(img_water)
        layer = Image.new('RGBA', im.size, (0,0,0,0))
        layer.paste(wm, (im.size[0] - offset_x, im.size[1] - offset_y))
        newIm = Image.composite(layer, im, layer)
        newIm.save(img_new)

    except Exception as e:
        print(">>>>>>>>>>> WaterMark EXCEPTION:  " + str(e))
        return False
    else:
        return True

def main():
    watermark("original.jpg", "watermark.png", "afterwater.jpg", 250, 50)

if __name__ == '__main__':
    main()