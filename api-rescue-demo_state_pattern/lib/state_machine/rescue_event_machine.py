#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from transitions import Machine
from lib.state_machine import event_states
from lib.state_machine import event_transitions
from datetime import datetime
from lib.state_machine import RescueEventModel
from lib.state_machine import StateAwaitOrder


class RescueEventMachine(object):
    """
    此类目的是为了方便使用语法提示，做了一层封装
    """

    def __init__(self, default_state=StateAwaitOrder.value):
        self.model = RescueEventModel()
        Machine(self.model,
                states=event_states,
                transitions=event_transitions,
                send_event=True,
                initial=default_state)

    def alarm(self, event_id: str, ev_id: int, date_time: datetime, source: str) -> None:
        self.model.alarm(event_id=event_id, ev_id=ev_id, date_time=date_time, source=source)

    def init(self, event_id: str) -> None:
        self.model.init(event_id=event_id)

    def check_notice(self, event_id: str) -> None:
        self.model.check_notice(event_id=event_id)

    def arrived(self, event_id: str) -> None:
        self.model.arrived(event_id=event_id)

    def sign_in(self, event_id: str) -> None:
        self.model.sign_in(event_id=event_id)

    def answer_timeout(self, event_id: str) -> None:
        self.model.answer_timeout(event_id=event_id)

    def sign_in_timeout(self, event_id: str) -> None:
        self.model.sign_in_timeout(event_id=event_id)

    def send_message(self, event_id: str) -> None:
        self.model.send_message(event_id=event_id)
