#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.common import application
from lib.common import config
from flask import jsonify
import services


@application.route('/doAlarm', methods=['GET'])
def do_alarm():
    return jsonify(services.do_alarm())


@application.route('/doCheck', methods=['GET'])
def do_check():
    return jsonify(services.do_check())


@application.route('/doArrived', methods=['GET'])
def do_arrive():
    return jsonify(services.do_arrived())


@application.route('/getEventLevel', methods=['GET'])
def get_event_level():
    return jsonify(services.get_event_level())


@application.route('/getEventState', methods=['GET'])
def get_event_state():
    return jsonify(services.get_event_state())


@application.route('/sendmessage', methods=['GET'])
def send_message():
    """
    动作-报警::
    * URL：/send_message
    * 请求方法： GET
    * 请求参数： evId=8adc3a22-d77d-11e9-888d-b8868799fb3c
    * 返回值：
    :return:
        [source, json]
        {
            "Code": 0,
            "EventId": 10987
        }
    """
    return jsonify(services.send_message())


if __name__ == "__main__":
    application.run(
        host=config.listen,
        port=config.port,
        debug=config.debug
    )
