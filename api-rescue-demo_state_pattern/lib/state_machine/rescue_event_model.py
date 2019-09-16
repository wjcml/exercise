#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
from db_model import RescueEvent
from db_model import AlarmInfo
from lib.common import db_session
from lib.state_machine import StateInit
from lib.state_machine import StateL1RescueDispatch
from lib.state_machine import StateL1RescueAnswer
from lib.state_machine import StateL1RescueSignIn
from lib.state_machine import StateL2RescueDispatch
from lib.state_machine import StateL2RescueAnswer
from lib.state_machine import StateL2RescueSignIn
from lib.state_machine import StateL3RescueDispatch
from lib.state_machine import StateComplete
from lib.state_machine import StateSendMsg
import uuid


class RescueEventModel(object):
    def __init__(self):
        self.ev_id: int = 0
        self.date_time: datetime = datetime.now()
        self.source: str = 'Nano'

    @staticmethod
    def get_event_id(event):
        return event.kwargs.get('event_id', str(uuid.uuid1()))

    @staticmethod
    def after_init(event):
        event_id = RescueEventModel.get_event_id(event)

        alarm_info = AlarmInfo()
        alarm_info.uuid = str(uuid.uuid1())
        alarm_info.row_time = event.kwargs.get('date_time', '1970-01-01 00:00:00')
        alarm_info.ev_id = event.kwargs.get('ev_id')
        alarm_info.source = event.kwargs.get('source', 'Nano')
        db_session.add(alarm_info)

        rescue_event = RescueEvent()
        rescue_event.uuid = event_id
        rescue_event.alarm_id = alarm_info.uuid
        rescue_event.row_time = event.kwargs.get('date_time', '1970-01-01 00:00:00')
        rescue_event.state = StateInit.value
        rescue_event.state_time = rescue_event.row_time
        db_session.add(rescue_event)

        db_session.commit()
        print('L0：报警成功。请耐心等待救援！')

    @staticmethod
    def after_level1_dispatch(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateL1RescueDispatch.value

        db_session.commit()
        print('L1：进入一级救援阶段，系统自动派单完成。')

    @staticmethod
    def after_level1_answer(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateL1RescueAnswer.value

        db_session.commit()
        print('L1：救援人员已经接警。')

    @staticmethod
    def after_level1_sign_in(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateL1RescueSignIn.value

        db_session.commit()
        print('L1：救援人员已经到达现场。')

    @staticmethod
    def after_level1_complete(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateComplete.value

        db_session.commit()

        print('L1：一级救援完成。')

    @staticmethod
    def after_level2_dispatch(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateL2RescueDispatch.value

        db_session.commit()
        print('L2：进入二级救援阶段，系统自动派单完成。')

    @staticmethod
    def after_level2_answer(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateL2RescueAnswer.value

        db_session.commit()
        print('L2：救援人员已经接警。')

    @staticmethod
    def after_level2_sign_in(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateL2RescueSignIn.value

        db_session.commit()
        print('L2：救援人员已经到达现场。')

    @staticmethod
    def after_level2_complete(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateComplete.value

        db_session.commit()
        print('L2：二级救援完成。')

    @staticmethod
    def after_level3_dispatch(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateL3RescueDispatch.value

        db_session.commit()
        print('L3：一级、二级救援失效，救援事件已经进入三级救援阶段，请及时联系 110 或 119 处理。')

    @staticmethod
    def after_complete(event):
        event_id = RescueEventModel.get_event_id(event)

        inited_event = db_session.query(RescueEvent).filter(RescueEvent.uuid == event_id).first()
        inited_event.state = StateComplete.value

        db_session.commit()
        print('救援任务完成。')

    @staticmethod
    def after_send_message(event):
        event_id = RescueEventModel.get_event_id(event)
        print(" ")
        print(event_id)
        print('发送消息成功。')
        print(" ")


