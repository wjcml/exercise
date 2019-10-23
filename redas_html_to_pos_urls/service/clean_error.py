import logging
import os
import re
import time


def save_html_log_for_urls(html, platform, spiderUuid, url, e):
    time_ticks = time.strftime("%Y%m%d%H%M%S", time.localtime())
    now = time.strftime("%Y_%m_%d", time.localtime())
    is_ture = True

    if platform == "拉勾":
        pattern = ".*?com/(.*)"
        html_path = "../error/html/lagou/" + now
        log_path = "../error/log/lagou"
    elif platform == "boss直聘":
        pattern = ".*?com/(.*)"
        html_path = "../error/html/zhipin/" + now
        log_path = "../error/log/zhipin"
    else:
        pattern = ""
        html_path = ""
        log_path = ""
        is_ture = False

    if is_ture:
        src_url_pos_sign = re.search(pattern, url).group(1).strip().replace("/", "_").replace("?", "_")

        if not os.path.exists(html_path):
            os.makedirs(html_path)

        if not os.path.exists(log_path):
            os.makedirs(log_path)

        # 将出错的html写入文件
        file_url_name = html_path + "/" + src_url_pos_sign + "_" + time_ticks + ".html"
        with open(file_url_name, "w", encoding="utf-8") as file:
            file.write(html)
            file.close()

        # 打印错误日志
        log_file_url_name = log_path + "/" + "error.log"
        to_log = logging.FileHandler(filename=log_file_url_name, encoding="utf-8")
        logging.basicConfig(handlers=[to_log],
                            level=logging.ERROR,
                            format="%(asctime)s - %(levelname)s - %(message)s",
                            datefmt="%Y/%m/%d %H:%M:%S %p")
        logging.error("spiderUuid: " + spiderUuid)
        logging.error("url: " + url)
        logging.error("html文件保存到：" + file_url_name.replace("../", ""))
        logging.error("详情：" + str(e))
        logging.error("=======================================================================================")
