import json

from kafka import KafkaConsumer
from configparser import ConfigParser

from data_clean.lagou_url_clean import LagouUrlClean
from data_clean.zhipin_url_clean import ZhipinUrlClean


def main():
    config = ConfigParser()
    config.read("../config/mq_config.ini", encoding='UTF-8')
    host = config['mq_positions_url_html']["host"]
    group = config['mq_positions_url_html']["group"]
    topic = config['mq_positions_url_html']["topic"]

    while True:
        consumer = KafkaConsumer(topic,
                                 group_id=group,
                                 bootstrap_servers=[host])
        for message in consumer:
            # print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
            #                                      message.offset, message.key,
            #                                      message.value))

            json_string = message.value.decode("utf-8")
            load_dict = json.loads(json_string)
            if load_dict["platform"] == "拉勾":
                result = LagouUrlClean(load_dict)
                result.data_clean()
            elif load_dict["platform"] == "boss直聘":
                result = ZhipinUrlClean(load_dict)
                result.data_clean()


if __name__ == "__main__":
    main()
