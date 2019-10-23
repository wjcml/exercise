import base64

from bs4 import BeautifulSoup

from api_consumer.send_info import send_to_api
from data_clean.platform_data_clean import PlatformDataClean
from service.clean_error import save_html_log_for_urls


class ZhipinUrlClean(PlatformDataClean):
    def __init__(self, load_dict):
        super().__init__()
        self.load_dict = load_dict

    def data_clean(self):

        position_url_list = []

        html = base64.b64decode(self.load_dict["htmlString"].encode("utf-8")).decode("utf-8")

        try:
            soup = BeautifulSoup(html, "lxml")
            tag_a_list = soup.select(".job-list > ul > li > div > div.info-primary > h3 > a")
            for tag_a in tag_a_list:
                position_url_list.append("https://www.zhipin.com" + tag_a["href"])

            print(position_url_list)

            send_data = {"sourceUrl": self.load_dict["url"], "urls": position_url_list}
            send_to_api("send_url", send_data)

        except Exception as e:
            try:
                platform = self.load_dict.get("platform")
                spiderUuid = self.load_dict.get("spiderUuid")
                url = self.load_dict.get("url")
                print(url)
                save_html_log_for_urls(html, platform, spiderUuid, url, e)
            except Exception as exc:
                print(exc)


if __name__ == "__main__":
    zhipin = ZhipinUrlClean("l")
    zhipin.data_clean()
