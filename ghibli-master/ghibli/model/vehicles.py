#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from model.init_model import DBModelBase


class Vehicles(DBModelBase):
    __tablename__ = 'vehicles'

    id = Column(Integer(), primary_key=True)
    film_id = Column(String(255))
    url = Column(String(255))
