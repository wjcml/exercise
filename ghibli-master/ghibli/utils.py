#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from common import session
from model import Film
from model import Location
from model import People
from model import Specie
from model import Vehicle


# def add_location(film_id: str, url: str):
#     location = Location(film_id=film_id, url=url)
#     session.add(location)
#
#
# def add_people(film_id: str, url: str):
#     people = People(film_id=film_id, url=url)
#     session.add(people)
#
#
# def add_specie(film_id: str, url: str):
#     specie = Specie(film_id=film_id, url=url)
#     session.add(specie)
#
#
# def add_vehicle(film_id: str, url: str):
#     vehicle = Vehicle(film_id=film_id, url=url)
#     session.add(vehicle)


def add_url_rows(class_name: str, film_id: str, url_list: list):
    """
    使用统一代码为相同表结构的表增加表记录
    :param class_name: 表模型的类名称
    :param film_id: 电影编号
    :param url_list: URL列表
    :return: None
    """
    for url in url_list:
        # Vehicle(film_id="5fdfb320-2a02-49a7-94ff-5ca418cae602", url="https://ghibliapi.herokuapp.com/vehicles/")
        row = eval('%s(film_id="%s", url="%s")' % (class_name, film_id, url))
        session.add(row)


def get_urls(class_name: str, film_id: str):
    """
    使用统一代码查询相同表结构的表记录
    :param class_name: 表模型的类名称
    :param film_id: 电影编号
    :return: None
    """
    # session.query(People).filter(People.film_id == film_id).all()
    objs = eval('session.query(%s).filter(%s.film_id == "%s").all()'
                    % (class_name, class_name, film_id))

    url_list = list()

    for obj in objs:
        url_list.append(obj.url)

    return url_list
