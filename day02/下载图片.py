import urllib.request
from bs4 import BeautifulSoup
import os

url = "http://www.win4000.com/wallpaper_detail_142158_1.html"
res = urllib.request.urlopen(url)
html = res.read().decode("utf-8")
bf = BeautifulSoup(html, features="html.parser")
picTitle = bf.find("div", class_="ptitle").find("h1").text
picUrl = bf.find("div", class_="paper-down").find("a").get("href")
print(picUrl)
# 创建文件夹
folder = os.path.exists("E:\\123\\"+picTitle)

if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
    os.makedirs("E:\\123\\"+picTitle)  # makedirs 创建文件时如果路径不存在会创建这个路径
    print("创建成功")
else:
    pass

s = picUrl.split("/")[len(picUrl.split("/"))-1]
zpName = s.split("?")[0]
print(zpName)

