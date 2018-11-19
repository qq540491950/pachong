import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
}
res = requests.get("http://i.meizitu.net/2018/11/16a01.jpg", headers=headers)
with open("./a.jpg", "wb") as f:
    f.write(res)
