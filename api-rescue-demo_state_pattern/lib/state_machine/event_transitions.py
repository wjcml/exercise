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


event_transitions = [
    {
        'trigger': 'alarm',
        'source': StateAwaitOrder.value,
        'dest': StateInit.value,
        'after': 'after_init'
    },
    {
        'trigger': 'init',
        'source': StateInit.value,
        'dest': StateL1RescueDispatch.value,
        'after': 'after_level1_dispatch'
    },
    {
        # 一级救援：点击微信报警消息，变更为一级接警状态
        'trigger': 'check_notice',
        'source': StateL1RescueDispatch.value,
        'dest': StateL1RescueAnswer.value,
        'after': 'after_level1_answer'
    },
    {
        # 一级救援：救援人员接警后在指定时间到达现场，变更为一级签到状态
        'trigger': 'arrived',
        'source': StateL1RescueAnswer.value,
        'dest': StateL1RescueSignIn.value,
        'after': 'after_level1_sign_in'
    },
    {
        # 一级救援：签到后，变更为完成状态
        'trigger': 'sign_in',
        'source': StateL1RescueSignIn.value,
        'dest': StateComplete.value,
        'after': 'after_level1_complete'
    },
    {
        # 一级救援：微信报警消息在指定时间内，无人点击（未接警），进入二级救援阶段，变更为二级指派状态
        'trigger': 'answer_timeout',
        'source': StateL1RescueDispatch.value,
        'dest': StateL2RescueDispatch.value,
        'after': 'after_level2_dispatch'
    },
    {
        # 一级救援：救援人员接警后在指定时间内未达到现场，进入二级救援阶段，变更为二级指派状态
        'trigger': 'sign_in_timeout',
        'source': StateL1RescueSignIn.value,
        'dest': StateL2RescueDispatch.value,
        'after': 'after_level2_dispatch'
    },
    {
        # 二级救援：点击微信报警消息，变更为二级接警状态
        'trigger': 'check_notice',
        'source': StateL2RescueDispatch.value,
        'dest': StateL2RescueAnswer.value,
        'after': 'after_level2_answer'
    },
    {
        # 二级救援：救援人员到达现场，变更为二级签到状态
        'trigger': 'arrived',
        'source': StateL2RescueAnswer.value,
        'dest': StateL2RescueSignIn.value,
        'after': 'after_level2_sign_in'
    },
    {
        # 二级救援：签到后，变更为完成状态
        'trigger': 'sign_in',
        'source': StateL2RescueSignIn.value,
        'dest': StateComplete.value,
        'after': 'after_level2_complete'
    },
    {
        # 二级救援：微信报警消息在指定时间内，无人点击（未接警），进入三级救援阶段，变更为三级指派状态
        'trigger': 'answer_timeout',
        'source': StateL2RescueDispatch.value,
        'dest': StateL3RescueDispatch.value,
        'after': 'after_level3_dispatch'
    },
    {
        # 二级救援：微信报警消息在指定时间内，无人点击（未接警），进入三级救援阶段，变更为三级指派状态
        'trigger': 'sign_in_timeout',
        'source': StateL2RescueAnswer.value,
        'dest': StateL3RescueDispatch.value,
        'after': 'after_level3_dispatch'
    },
    {
        # 救援完成：不管当前处于任何状态，触发完成动作时，状态变更为救援完成
        'trigger': 'complete',
        'source': '*',
        'dest': StateComplete.value,
        'after': 'after_complete'
    },
    {
        'trigger': 'send_message',
        'source': '*',
        'dest': StateSendMsg.value,
        'after': 'after_send_message'
    }
]
