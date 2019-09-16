#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from happy_utils import HappyPyException


def make_api_respone(code: int, message: str, data=None):
    """
    构造接口响应内容

    :rtype:
    :param code: 响应代码
    :param message: 消息
    :param data:  返回内容
    :return: dict
    """

    if data is None:
        data = {}

    if not isinstance(data, dict):
        raise HappyPyException('参数 data 类型必须为 dict')

    res = {
        'code': code,
        'message': message if message else '',
        'obj': data if data else '{}'
    }

    return res
