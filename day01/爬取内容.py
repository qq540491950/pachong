import urllib.request
from bs4 import BeautifulSoup


url = "http://www.quanshuwang.com/book/160/160589/43013728.html"
res = urllib.request.urlopen(url)
html = res.read().decode("gbk")
bf = BeautifulSoup(html, features="html.parser")
# 删除js、css内容
for script in bf(["script", "style"]):
    script.extract()
content = bf.find_all("div", id="content")[0].text.replace('\xa0'*8, '\n\n')
print(content)
