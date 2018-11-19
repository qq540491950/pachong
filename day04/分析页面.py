import requests
from bs4 import BeautifulSoup

url = "http://www.mzitu.com/158305/45"
res = requests.get(url)
html = res.text
bf = BeautifulSoup(html, features="html.parser")
# 获取最大页数
maxNum = bf.find("div", class_="pagenavi").find_all("a")[-2:-1][0].find("span").text
print(maxNum)
# 获取标题
title = bf.find("h2", class_="main-title").text
print(title)
# 王雨纯警花制服诱惑 娇喘连连让人乖乖缴械投降
