#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import inspect
import re
import uuid
from flask import request
from happy_utils import ParameterManager
from lib.utils import make_api_respone
from lib.common import hlog
from lib.state_machine import RescueEventMachine

ARG_FLAG_EV_ID = 1 << 0
ARG_FLAG_DATE_TIME = 2 << 0
ARG_FLAG_SOURCE = 3 << 0


def validate_ev_id(value: str) -> bool:
    """
    验证电梯编号
    :param str value:
    :return: bool
    """

    return value and len(value) >= 3


def validate_date_time(value: str) -> bool:
    """
    验证日期格式，比如 2018-10-11 10:24:35
    :param str value:
    :return: bool
    """

    match_obj = re.match('^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}$', value)

    return True if match_obj else False


def validate_source(value: str) -> bool:
    """
    验证报警来源
    :param str value:
    :return: bool
    """

    if value == 'Nano':
        return True
    elif value == 'Mix':
        return True
    elif value == 'WeChat':
        return True
    else:
        return False


pm = ParameterManager()
pm.register_para(ARG_FLAG_EV_ID, 'evId', validate_ev_id)
pm.register_para(ARG_FLAG_DATE_TIME, 'dateTime', validate_date_time)
pm.register_para(ARG_FLAG_SOURCE, 'source', validate_source)


def do_alarm():
    func_name = inspect.stack()[0][3]
    hlog.enter_func(func_name)

    pm.enable_paras(ARG_FLAG_EV_ID | ARG_FLAG_DATE_TIME | ARG_FLAG_SOURCE)

    result = pm.validate_paras(request.args)

    if not result[0]:
        hlog.exit_func(func_name)
        return make_api_respone(1, result[1])

    ev_id = request.args.get('evId')
    date_time = datetime.strptime(request.args.get('dateTime'), '%Y-%m-%d %H:%M:%S')
    source = request.args.get('source')

    # 优先生成救援事件编号，解决状态机框架无返回值问题，用作后续事件跟踪
    event_id = str(uuid.uuid1())

    hlog.var('event_id', ev_id)
    hlog.var('ev_id', ev_id)
    hlog.var('date_time', date_time)
    hlog.var('source', source)

    rescue_event = RescueEventMachine()
    rescue_event.alarm(event_id, ev_id, date_time, source)
    rescue_event.init(event_id)

    result = {
        "code": 0,
        "EventId": event_id
    }

    hlog.var('result', result)

    hlog.exit_func(func_name)
    return result
