import base64
import datetime
import re
from pprint import pprint

from bs4 import BeautifulSoup

from api_consumer.post_urls import send_to_api
from data_clean.platform_data_clean import PlatformDataClean
from service.clean_error import save_html_log


class LagouDetailClean(PlatformDataClean):
    def __init__(self, load_dict):
        super().__init__()
        self.load_dict = load_dict

    def data_clean(self):

        html = base64.b64decode(self.load_dict["htmlString"].encode("utf-8")).decode("utf-8")
        try:
            soup = BeautifulSoup(html, "lxml")

            # 职位
            position_list = soup.select(".job-name .name")
            is_position = re.search(".*?>(.*?)</.*?", str(position_list[0]))
            if is_position:
                position = is_position.group(1).strip()
            else:
                position = ""

            # 薪资，经验，学历
            money_location_exp_edu = soup.select(".job_request span")
            is_salary = re.search(".*?>(.*?)</.*?", str(money_location_exp_edu[0]))
            if is_salary:
                salary = is_salary.group(1).replace("/", "").strip()
            else:
                salary = ""

            is_city = re.search(".*?>(.*?)</.*?", str(money_location_exp_edu[1]))
            if is_city:
                city = is_city.group(1).replace("/", "").strip()
            else:
                city = ""

            is_exp = re.search(".*?>(.*?)</.*?", str(money_location_exp_edu[2]))
            if is_exp:
                exp = is_exp.group(1).replace("/", "").strip()
            else:
                exp = ""

            is_edu = re.search(".*?>(.*?)</.*?", str(money_location_exp_edu[3]))
            if is_edu:
                edu = is_edu.group(1).replace("/", "").strip()
            else:
                edu = ""

            # 职位标签
            tags = soup.select(".position-label li")
            tag_list = []
            for tag in tags:
                is_t = re.search(".*?>(.*?)</.*?", str(tag))
                if is_t:
                    t = is_t.group(1).strip()
                    tag_list.append(t)

            # 职位诱惑
            advantage = []
            is_advantage_str = re.search(".*?>(.*?)</.*?", str(soup.select(".job-advantage p")[0]))
            if is_advantage_str:
                advantagestr = is_advantage_str.group(1)
            else:
                advantagestr = "等"
            advantage_str = advantagestr.replace("等", "")
            adv_pattern = re.compile(u"\w+")
            adv_result = re.findall(adv_pattern, advantage_str)
            if adv_result:
                for adv in adv_result:
                    advantage.append(adv)

            # 职位描述
            pos_describ_s = soup.select(".job-detail p")
            pos_desc_list = []
            for pos_desc in pos_describ_s:
                is_p_d = re.search(".*?>(.*?)</.*?", str(pos_desc))
                if is_p_d:
                    p_d = is_p_d.group(1)
                else:
                    p_d = ""
                pos_desc_list.append(p_d.strip())
            pos_desc_str = "".join(pos_desc_list)
            pos_desc = pos_desc_str.replace("<br/>", "").replace("\xa0", "")

            # 招聘者
            hr_name = soup.select(".hr_name")[0]["value"]
            hr_position = soup.select(".hr_position")[0]["value"]

            # 公司
            is_company = re.search(".*?>(.*?)</.*?", str(soup.select(".job-name .company")[0]))
            if is_company:
                company = is_company.group(1)
            else:
                company = "招聘"
            company_name = company.replace("招聘", "").strip()

            # 上班地点
            work_place_list = re.findall(".*?>(.*?)<.*?", str(soup.select(".work_addr")[0]), re.S)
            work_place_str = "".join(work_place_list[0:-2])
            location = work_place_str.replace("\n", "").replace(" ", "")

            # 公司性质
            company_nature = []
            is_company_nature_str = re.search(".*?>(.*?)</.*?", str(soup.select(".c_feature_name")[0]))
            if is_company_nature_str:
                company_nature_str = is_company_nature_str.group(1)
            else:
                company_nature_str = ""
            nature_pattern = re.compile(u"\w+")
            nature_result = re.findall(nature_pattern, company_nature_str)
            if nature_result:
                for nature in nature_result:
                    company_nature.append(nature.strip())

            # 发展阶段
            is_stage = re.search(".*?>(.*?)</.*?", str(soup.select(".c_feature_name")[1]))
            if is_stage:
                stage = is_stage.group(1)
            else:
                stage = ""

            # 规模
            is_scale = re.search(".*?>(.*?)</.*?", str(soup.select(".c_feature_name")[2]))
            if is_scale:
                scale = is_scale.group(1)
            else:
                scale = ""

            # 公司主页
            company_main_page = str(soup.select(".c_feature li a")[0]["href"])

            # 发布时间
            is_time = re.search(".*?>(.*?)</.*?", str(soup.select(".publish_time")[0]))
            if is_time:
                this_time = is_time.group(1)
                publish_time = this_time.split(" ")[0].strip()
                publish_time = time_handle(publish_time)
            else:
                publish_time = ""

            # 来源
            src_name = self.load_dict.get("platform")
            src_url = self.load_dict.get("url")
            src_pos_id = str(soup.select(".resume-deliver a")[0]["data-position-id"])

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


def time_handle(publish_time):
    _hour = re.search(":", publish_time)
    _day = re.search("天", publish_time)
    _date = re.search("-", publish_time)

    now = datetime.datetime.now()
    if _hour:
        return now.strftime("%Y-%m-%d")
    if _day:
        days_ago = re.search("\d+", publish_time).group()
        delta = datetime.timedelta(days=int(days_ago))
        return (now - delta).strftime("%Y-%m-%d")
    return now.strftime("%Y-%m-%d")


if __name__ == "__main__":
    lagou = LagouDetailClean("l")
    lagou.data_clean()
