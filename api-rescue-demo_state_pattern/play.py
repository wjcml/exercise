#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import uuid
from datetime import datetime

import requests

base_url = 'http://127.0.0.1:2566'


def do_alarm():
    ev_id = uuid.uuid1()
    url = \
        base_url + '/doAlarm?evId=' + str(ev_id) + \
        '&dateTime=' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '&source=Nano'
    r = requests.get(url)

    if r.status_code == 200:
        return_value = r.json()

        print('A. 报警成功')
        print('A. \t返回信息：\n\t\t%s' % return_value)

        _event_id = return_value['EventId']
    else:
        print('A. 报警失败')
        sys.exit(1)

    return _event_id


def get_event_level(_event_id: str):
    url = base_url + '/getEventLevel?eventId=' + event_id
    r = requests.get(url)

    if r.status_code == 200:
        return_value = r.json()

        print('Check1. 查询当前救援等级成功')
        print('Check1. \t返回信息：\n\t\t%s' % return_value)
    else:
        print('Check1. 查询当前救援等级失败')
        sys.exit(1)


def get_event_state(_event_id: str):
    url = base_url + '/getEventState?eventId=' + event_id
    r = requests.get(url)

    if r.status_code == 200:
        return_value = r.json()

        print('Check2. 查询当前救援状态成功')
        print('Check2. \t返回信息：\n\t\t%s' % return_value)
    else:
        print('Check2. 查询当前救援状态失败')
        sys.exit(1)


def do_check(_event_id: str):
    url = base_url + '/doCheck?eventId=' + event_id
    r = requests.get(url)

    if r.status_code == 200:
        return_value = r.json()

        print('B. 救援人员已经接警')
        print('B. \t返回信息：\n\t\t%s' % return_value)
    else:
        print('B. 接警失败')
        sys.exit(1)


def do_arrived(_event_id: str):
    url = base_url + '/doArrived?eventId=' + event_id
    r = requests.get(url)

    if r.status_code == 200:
        return_value = r.json()

        print('C. 救援人员已经达到现场，救援完成')
        print('C. \t返回信息：\n\t\t%s' % return_value)
    else:
        print('C. 更新救援状态失败')
        sys.exit(1)


if __name__ == '__main__':
    event_id = do_alarm()

    get_event_level(event_id)
    get_event_state(event_id)

    do_check(event_id)
    do_arrived(event_id)
