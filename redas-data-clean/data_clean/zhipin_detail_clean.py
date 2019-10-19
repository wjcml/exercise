import base64
import re
from pprint import pprint

from bs4 import BeautifulSoup

from api_consumer.post_urls import send_to_api
from data_clean.platform_data_clean import PlatformDataClean
from service.clean_error import save_html_log


class ZhipinDetailClean(PlatformDataClean):
    def __init__(self, load_dict):
        super().__init__()
        self.load_dict = load_dict

    def data_clean(self):

        html = base64.b64decode(self.load_dict["htmlString"].encode("utf-8")).decode("utf-8")
        try:
            soup = BeautifulSoup(html, "lxml")

            # 职位
            position_list = soup.select(".info-primary .name h1")
            is_position = re.search(".*?>(.*?)</.*?", str(position_list[0]))
            if is_position:
                position = is_position.group(1).strip()
            else:
                position = ""

            # 薪资
            salary_list = soup.select(".info-primary .name .salary")
            is_salary = re.search(".*?>(.*?)</.*?", str(salary_list[0]))
            if is_salary:
                salary = is_salary.group(1).strip()
            else:
                salary = ""

            # 城市，经验，学历
            city_exp_edu = re.findall(".*?>(.*?)<.*?", str(soup.select(".info-primary p")[0]), re.S)
            if city_exp_edu:
                city = city_exp_edu[0].strip()
                exp = city_exp_edu[2].strip()
                edu = city_exp_edu[4].strip()
            else:
                city = ""
                exp = ""
                edu = ""

            # 职位标签
            tag_list = []

            # 职位诱惑
            advantage = []
            advantage_list = list(set(soup.select(".tag-container .tag-more .job-tags span")))
            for adv_b in advantage_list:
                adv_result = re.search(".*?>(.*?)</.*?", str(adv_b))

                if adv_result:
                    advantage.append(adv_result.group(1))

            # 职位描述
            pos_describ_s = soup.select("div.detail-content > .job-sec > .text")
            is_pos_desc_str = re.search(".*?>(.*?)</.*?", str(pos_describ_s[0]), re.S)
            if is_pos_desc_str:
                pos_desc_str = is_pos_desc_str.group(1).strip()
                pos_desc = pos_desc_str.replace("<br/>", "").replace("&amp;", "&")
            else:
                pos_desc = ""

            # 招聘者
            is_hr_name = re.search(".*?>(.*?)<i.*?", str(soup.select(".detail-op .name")[0]))
            if is_hr_name:
                hr_name = is_hr_name.group(1).strip()
            else:
                hr_name = ""

            is_hr_position = re.search(".*?>(.*?)<em.*?", str(soup.select(".detail-op .gray")[0]))
            if is_hr_position:
                hr_position = is_hr_position.group(1).strip()
            else:
                hr_position = ""

            # 公司
            is_company_name = re.search(".*?>(.*?)</.*?", str(soup.select(".company-info > a")[1]), re.S)
            if is_company_name:
                company_name = is_company_name.group(1).strip()
            else:
                company_name = ""

            # 上班地点
            work_place = re.search(".*?>(.*?)<.*?", str(soup.select(".job-location .location-address")[0]))
            if work_place:
                location = work_place.group(1).strip()
            else:
                location = ""

            # 公司info
            stage, scale, company_main_page, publish_time = "", "", "", ""
            company_nature = []
            company_info_list = soup.select(".job-sider .sider-company p")
            for company_info in company_info_list:
                info_list = list(company_info)

                is_stage = re.search(".*?stage.*?", str(info_list[0]))
                is_scale = re.search(".*?scale.*?", str(info_list[0]))
                is_nature = re.search(".*?industry.*?", str(info_list[0]))
                is_main_page = re.search(".*?net.*?", str(info_list[0]))
                is_publish_time = re.search(".*?更新于.*?", str(info_list[0]))

                if is_stage:
                    # 发展阶段
                    stage = info_list[1].strip()
                    continue

                if is_scale:
                    # 规模
                    scale = info_list[1].strip()
                    continue

                if is_nature:
                    # 公司性质
                    company_nature = []
                    nature_str = re.search(".*?>(.*?)<.*?", str(info_list[1])).group(1)
                    nature_pattern = re.compile(u"\w+")
                    nature_result = re.findall(nature_pattern, nature_str)
                    for result in nature_result:
                        company_nature.append(result.strip())
                    continue

                if is_main_page:
                    # 主页
                    company_main_page = info_list[1].strip()
                    continue

                if is_publish_time:
                    # 发布时间
                    publish_time = re.search(".*?更新于：(.*)", str(info_list[0])).group(1).strip()
                    continue

            # 来源
            src_name = self.load_dict.get("platform")
            src_url = self.load_dict.get("url")
            src_pos_id = re.search(".*?detail/(.*?)\.html.*?", self.load_dict["url"]).group(1).strip()

            # spiderUuid
            spider_uuid = self.load_dict.get("spiderUuid")

            info = dict()
            info['srcName'] = src_name
            info['srcUrl'] = src_url
            info['srcPosId'] = src_pos_id
            info['position'] = position
            info['salary'] = salary
            info['location'] = location
            info['exp'] = exp
            info['edu'] = edu
            info['tagList'] = tag_list
            info['advantage'] = advantage
            info['posDesc'] = pos_desc
            info['hrName'] = hr_name
            info['hrPosition'] = hr_position
            info['companyName'] = company_name
            info['companyNature'] = company_nature
            info['stage'] = stage
            info['scale'] = scale
            info['companyMainPage'] = company_main_page
            info['publishTime'] = publish_time
            info['spiderUuid'] = spider_uuid

            send_data = info
            send_to_api("send_pos_detail", send_data)

        except Exception as e:
            try:
                platform = self.load_dict.get("platform")
                spiderUuid = self.load_dict.get("spiderUuid")
                url = self.load_dict.get("url")
                save_html_log(html, platform, spiderUuid, url, e)
            except Exception as exc:
                print(exc)


if __name__ == "__main__":
    zhipin = ZhipinDetailClean("l")
    zhipin.data_clean()
