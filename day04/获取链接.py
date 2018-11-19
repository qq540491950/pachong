import requests
from bs4 import BeautifulSoup

url = "http://www.mzitu.com/all"
res = requests.get(url)
html = res.text
bf = BeautifulSoup(html, features="html.parser")
urls = bf.find_all("p", class_="url")

for img_html in urls:
    bf1 = BeautifulSoup(str(img_html), features="html.parser")
    img_list = bf1.find_all("a")
    for img_url in img_list:
        img_url = img_url.get("href")
        print(img_url)
