import json
import logging
from configparser import ConfigParser

import requests


def send_to_api(api_config, data):
    try:
        config = ConfigParser()
        config.read("../config/api_config.ini", encoding='UTF-8')
        api_url = config['api_url_config'][api_config]

        headers = {
            "Content-Type": "application/json"
        }

        # 将解析的URL发送到addUrl的API接口
        response = requests.post(url=api_url,
                                 headers=headers,
                                 data=json.dumps(data))

        if response.status_code != requests.codes.ok:

            to_log = logging.FileHandler(filename="error.log", encoding="utf-8")
            logging.basicConfig(handlers=[to_log],
                                level=logging.ERROR,
                                format="%(asctime)s - %(levelname)s - %(message)s",
                                datefmt="%Y/%m/%d %H:%M:%S %p")

            logging.error(response.status_code)
            logging.error("=======================================================================================")

    except Exception as e:
        print(e)
