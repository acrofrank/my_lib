#coding:utf-8
import pytesseract
# pip3 install pillow
from PIL import Image

# 打开一个图片文件
im = Image.open('test.jpg')

data = pytesseract.image_to_string(im)

print (data)
