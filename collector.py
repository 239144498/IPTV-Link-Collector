import random
import re
import time

import requests
from urllib.parse import quote

request = requests.session()
start = 1  # 那一页开始
end = 2  # 那一页结束
key_words = "搜索关键字"
RE = r":&quot;(https://github\.com.*)&quot;}"  # 正则匹配

github_cookie = ""  # 输入你的GitHub Cookie
headers = {
    "Host": "github.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie": github_cookie
}

urls = set()

for i in range(start, end):
    url = f"https://github.com/search?p={i}&q={quote(key_words)}&type=Code"
    try:
        with request.get(url, headers=headers, timeout=10) as res:
            data = re.findall(RE, res.text)
            urls = urls | set(data)  # 链接去重
            time.sleep(random.uniform(0.5, 1.5))  # 随机延时
    except Exception as e:
        print(urls)
print(urls)
print("抓取链接总数:", len(urls))
with open("iptv.txt", "w") as f:
    f.write(str(urls))
