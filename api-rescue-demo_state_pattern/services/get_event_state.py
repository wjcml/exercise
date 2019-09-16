#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect
import re

from db_model import RescueEvent
from flask import request
from happy_utils import ParameterManager
from lib.utils import make_api_respone

from lib.common import hlog, db_session

ARG_FLAG_EVENT_ID = 1 << 0


def validate_event_id(value: str) -> bool:
    """
    验证事件编号
    :param str value: uuid
    :return: bool
    """

    match_obj = re.match('^\w{8}-\w{4}-\w{4}-\w{4}-\w{12}', value)

    return True if match_obj else False


pm = ParameterManager()
pm.register_para(ARG_FLAG_EVENT_ID, 'eventId', validate_event_id)


def get_event_state():
    func_name = inspect.stack()[0][3]
    hlog.enter_func(func_name)

    pm.enable_paras(ARG_FLAG_EVENT_ID)
    result = pm.validate_paras(request.args)

    if not result[0]:
        hlog.exit_func(func_name)
        return make_api_respone(1, result[1])

    event_id = request.args.get('eventId')
    hlog.var('event_id', event_id)

    rescue_event_obj = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
    event_state = str(rescue_event_obj.state)
    db_session.close()

    result = {
        "code": 0,
        "EventId": event_id,
        "EventState": event_state
    }

    hlog.var('result', result)

    hlog.exit_func(func_name)
    return result
