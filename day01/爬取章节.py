import urllib.request
from bs4 import BeautifulSoup

url = "http://www.quanshuwang.com/book/160/160589"
res = urllib.request.urlopen(url)
html = res.read().decode("gbk", "replace")
bf = BeautifulSoup(html, features="html.parser")
a_html = bf.find_all("div", class_="clearfix dirconone")[0].find_all("a")
for a in a_html:
    print(a.string, "===>", a.get("href"))
