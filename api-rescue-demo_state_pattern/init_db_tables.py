#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
执行初始化数据库表结构操作，请单独运行此文件代码
"""

from db_model.db_class_init import RescueDBBase
from lib.common import db_session
from lib.common import engine

# 如果没有导入表，那必须加载数据库模型包，才会创建表。


def drop_table(name: str):
    """
    从数据库删除表
    :param name: 表名称
    :return: None
    """
    if name:
        db_session.execute('DROP TABLE IF EXISTS ' + name)
        db_session.commit()


def create_tabls():
    """
    创建数据库表，如果表已经存在，则先删除
    :return: None
    """
    drop_table('alarm_info')
    drop_table('rescue_event')

    # 创建数据库表
    RescueDBBase.metadata.create_all(engine)


def main():
    create_tabls()


if __name__ == '__main__':
    main()
