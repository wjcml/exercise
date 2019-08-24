#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Text
from model.init_model import DBModelBase


class Films(DBModelBase):
    __tablename__ = 'films'

    id = Column(String(255), primary_key=True)
    title = Column(String(255))
    description = Column(Text())
    director = Column(String(255))
    producer = Column(String(255))
    release_date = Column(String(255))
    rt_score = Column(String(255))
    url = Column(String(255))
