#!/usr/bin/env python3
# -*- coding: utf-8 -*-

StateAwaitOrder=1
StateInit=2


class StateAwaitOrder(object):
    """
    一键报警或报警功能处于待命状态
    """
    value: str = '-1'
    level: int = -1


class StateInit(object):
    """
    用户执行报警动作，系统接受并响应该动作，并初始化应急救援事件
    """
    value: str = '0'
    level: int = 0


class StateL1RescueDispatch(object):
    """
    等待指派
    """
    value: str = '10'
    level: int = 1


class StateL1RescueAnswer(object):
    """
    救援人员接警
    """
    value: str = '11'
    level: int = 1


class StateL1RescueSignIn(object):
    """
    救援人员达到现场
    """
    value: str = '12'
    level: int = 1


class StateL2RescueDispatch(object):
    """
    等待指派
    """
    value: str = '20'
    level: int = 2


class StateL2RescueAnswer(object):
    """
    救援人员接警
    """
    value: str = '21'
    level: int = 2


class StateL2RescueSignIn(object):
    """
    救援人员达到现场
    """
    value: str = '22'
    level: int = 2


class StateL3RescueDispatch(object):
    """
    进入三级救援，提示拨打119或110
    """
    value: str = '30'
    level: int = 3


class StateComplete(object):
    """
    救援完成
    """
    value: str = '40'
    level: int = 4


class StateSendMsg(object):
    """
    发送消息
    """
    value: str = '50'
    level: int = 5
