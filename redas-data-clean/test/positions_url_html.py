import base64
import json

import requests


def main(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/"
                             "537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
               "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
               }
    response = requests.get(url=url, headers=headers)

    html = response.text

    info = dict()
    info["htmlString"] = base64.b64encode(html.encode("utf-8")).decode("utf-8")
    info["platform"] = "拉勾"
    info["url"] = url
    info["spiderUuid"] = "8a73615e-f09a-11e9-b191-b8868799fb3c"

    with open("lagou_detail.json", "w", encoding="utf-8") as f:
        json.dump(info, f)
        f.close()


if __name__ == "__main__":
    url = "https://www.lagou.com/jobs/1787334.html?show=a8911255e36549a8ab53f9afe7b528b5"
    main(url)
