import urllib.request
from bs4 import BeautifulSoup

num = [1, 2, 3, 4]
for i in num:
    print("第"+ str(i) + "次")
    url = "http://www.win4000.com/zt/heisi_" + str(i) + ".html"
    res = urllib.request.urlopen(url)
    html = res.read().decode("utf-8")
    bf = BeautifulSoup(html, features="html.parser")
    a_html = bf.find_all("div", class_="tab_box")[0].find_all("a")
    for a in a_html:
        # print(a.get("href"))
        a1 = a.get("href").split(".html")
        # print(a1[0])
        res1 = urllib.request.urlopen(a1[0] + ".html")
        html1 = res1.read().decode("utf-8")
        bf1 = BeautifulSoup(html1, features="html.parser")
        picNum = bf1.find("div", class_="ptitle").find("em").text
        picTitle = bf1.find("div", class_="ptitle").find("h1").text
        print(picTitle + "==> " + picNum)
        for i in range(1, int(picNum) + 1):
            print(a1[0] + "_" + str(i) + ".html")
