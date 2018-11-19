import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}


def get_page_index(offset, keyword):
    data = {
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": "20",
        "cur_tab": 3,
        "from": "gallery"
    }
    url = "https://www.toutiao.com/search_content/?" + urlencode(data)
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        print("请求索引出错")
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and "data" in data.keys():
        for item in data.get("data"):
            yield item.get("article_url")


def get_page_detail(url):
    try:
        res = requests.get(url,headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        print("请求详情出错")
        return None


def parse_page_detail(html):
    bf = BeautifulSoup(html, "lxml")
    title = bf.select("title")
    # images_pattern = re.compile('gallery: JSON.parse(.*?)', re.S)
    # print(images_pattern)
    print(title)


def main():
    html = get_page_index("0", "街拍")
    for url in parse_page_index(html):
        if url is not None:
            html1 = get_page_detail(url)
            parse_page_detail(html1)


if __name__ == '__main__':
    main()
