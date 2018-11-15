import urllib.request
from bs4 import BeautifulSoup
from time import time

class downloader(object):

    def __init__(self):
        # 文章目录地址
        self.server = "http://www.quanshuwang.com/book/160/160589"
        # 章节名
        self.names = []
        # 章节url
        self.urls = []
        # 章节数
        self.num = 0

    def get_download_url(self):
        res = urllib.request.urlopen(self.server)
        html = res.read().decode("gbk", "replace")
        bf = BeautifulSoup(html, features="html.parser")
        a_html = bf.find_all("div", class_="clearfix dirconone")[0].find_all("a")
        self.num = len(a_html)
        for a in a_html:
            # print(a.string, "===>", a.get("href"))
            self.names.append(a.string)
            self.urls.append(a.get("href"))

    def get_content(self, url):
        res = urllib.request.urlopen(url)
        html = res.read().decode("gbk")
        bf = BeautifulSoup(html, features="html.parser")
        # 删除js、css内容
        for script in bf(["script", "style"]):
            script.extract()
        content = bf.find_all("div", id="content")[0].text.replace('\xa0' * 8, '\n\n')
        return content

    def write_text(self, name, path, content):
        with open(path, "a", encoding="utf-8") as f:
            f.write(name + "\n")
            f.writelines(content)
            f.write("\n\n")


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    start = time()
    for i in range(dl.num):
        if dl.urls[i] != ' ':
            dl.write_text(dl.names[i], "这个道士不好惹.txt", dl.get_content(dl.urls[i]))
            print(dl.names[i], "下载完毕")
    stop = time()
    print("用时" + str(stop-start) + "秒")
    print("《这个道士不好惹》下载完毕")
