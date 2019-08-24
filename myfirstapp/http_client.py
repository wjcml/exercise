#!/usr/bin/env python3

import requests


headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


r = requests.get('http://localhost:5000', headers=headers)

print("返回代码：%s" % r.status_code)
print("网页字符编码：%s" % r.encoding)
print("响应头：%s" % r.headers)


with open('web_page.html', 'w') as f:
	f.write(r.text)
