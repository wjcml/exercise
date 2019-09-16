#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from db_model.db_class_init import RescueDBBase
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import String


class AlarmInfo(RescueDBBase):
    """
    报警信息
    """

    __tablename__ = 'alarm_info'
    uuid = Column(String(255), primary_key=True)
    row_time = Column(DateTime, default=None)
    ev_id = Column(String(255), default=None)
    source = Column(String(255), default=None)

    def __init__(self):
        self.__table__ = None

    def get_columns(self):
        return [col.name for col in self.__table__.columns]

    def to_dict(self):
        return dict([(col, getattr(self, col)) for col in self.get_columns()])
