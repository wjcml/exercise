#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.state_machine import StateAwaitOrder
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


event_states = [
    # 待命
    StateAwaitOrder.value,

    # 事件初始化
    StateInit.value,

    # 一级救援
    StateL1RescueDispatch.value,
    StateL1RescueAnswer.value,
    StateL1RescueSignIn.value,

    # 二级救援
    StateL2RescueDispatch.value,
    StateL2RescueAnswer.value,
    StateL2RescueSignIn.value,

    # 三级救援
    StateL3RescueDispatch.value,

    # 完成
    StateComplete.value,

    # 发送消息
    StateSendMsg.value
]
