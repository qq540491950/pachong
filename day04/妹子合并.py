import requests
import os
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}


class DownLoadImg(object):

    def __init__(self):
        self.server = "http://www.mzitu.com/all"
        self.urls = []
        self.path = "E:\\789\\"
        self.maxNum = 0
        self.title = ""

    # 获取图片页面
    def get_index_urls(self):
        res = requests.get(self.server, headers=headers)
        html = res.text
        bf = BeautifulSoup(html, features="html.parser")
        urls = bf.find_all("p", class_="url")

        for img_html in urls:
            bf1 = BeautifulSoup(str(img_html), features="html.parser")
            img_list = bf1.find_all("a")
            for img_url in img_list:
                img_url = img_url.get("href")
                self.urls.append(img_url)

    # 获取最大数页码，和标题
    def get_img_info(self, url):
        res = requests.get(url, headers=headers)
        html = res.text
        bf = BeautifulSoup(html, features="html.parser")
        # 获取最大页数
        maxNum = bf.find("div", class_="pagenavi").find_all("a")[-2:-1][0].find("span").text
        title = bf.find("h2", class_="main-title").text.strip().replace("!", "").replace(":", "").replace("?", "")
        self.maxNum = maxNum
        self.title = title

    # 获取图片链接
    def download_img(self, url, headers, title):
        res = requests.get(url, headers)
        html = res.text
        bf = BeautifulSoup(html, features="html.parser")
        img_url = bf.find("div", class_="main-image").find("img").get("src")
        img_name = img_url.split("/")[len(img_url.split("/"))-1]
        r = requests.get(img_url, headers=headers)
        with open(self.path + title + "\\" + img_name, "wb") as f:
            f.write(r.content)
        print(self.path + title + img_name + "下载成功")

    # 创建文件夹
    def makedir_folder(self, tiltle):
        # 创建文件夹
        folder = os.path.exists(self.path + tiltle)
        if not folder:
            os.makedirs(self.path + tiltle)
            print(self.path + tiltle + "创建成功")
        else:
            pass


if __name__ == '__main__':
    dimg = DownLoadImg()
    print("下载开始。。。")
    start = time.time()
    dimg.get_index_urls()
    for url in dimg.urls:
        dimg.get_img_info(url)
        # print(dimg.maxNum, dimg.title)
        dimg.makedir_folder(dimg.title)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            "Referer": url
        }
        for i in range(1, int(dimg.maxNum)):
            # print(url + "/" + str(i))
            dimg.download_img(url + "/" + str(i), headers, dimg.title)
    stop = time.time()
    print("下载完成用时：" + str(stop-start) + "秒")
