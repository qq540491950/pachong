import urllib.request
from bs4 import BeautifulSoup

url = "http://www.win4000.com/wallpaper_detail_142158"
res = urllib.request.urlopen(url + ".html")
html = res.read().decode("utf-8")
bf = BeautifulSoup(html, features="html.parser")
picNum = bf.find("div", class_="ptitle").find("em").text
print(picNum)
for i in range(1, int(picNum)+1):
    print(url + "_" + str(i) + ".html")
