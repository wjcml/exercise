#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
执行初始化数据库表结构操作，请单独运行此文件代码
"""

from model.init_model import DBModelBase
from common import engine
from common import session

# 如果没有导入表，那必须加载数据库模型包，才会创建表。

from model import Film

import json


def create_tabls():
    """
    创建数据库表，如果表已经存在，则先删除
    :return: None
    """
    drop_table('films')
    drop_table('locations')
    drop_table('people')
    drop_table('species')
    drop_table('vehicles')

    # 创建数据库表
    DBModelBase.metadata.create_all(engine)


def drop_table(name: str):
    """
    从数据库删除表
    :param name: 表名称
    :return: None
    """
    if name:
        session.execute('DROP TABLE IF EXISTS ' + name)
        session.commit()


def init_data_of_tables():
    """
    从JSON文件初始化表数据
    :return: None
    """
    from utils import add_url_rows

    with open('films.json', encoding="utf-8") as f:
        film_list = json.load(f)

        for film_info in film_list:
            film = Film(id=film_info["id"],
                        title=film_info["title"],
                        description=film_info["description"],
                        director=film_info["director"],
                        producer=film_info["producer"],
                        release_date=film_info["release_date"],
                        rt_score=film_info["rt_score"],
                        url=film_info["url"])
            session.add(film)

            location_list = film_info["locations"]
            add_url_rows('Location', film.id, location_list)

            people_list = film_info["people"]
            add_url_rows('People', film.id, people_list)

            specie_list = film_info["species"]
            add_url_rows('Specie', film.id, specie_list)

            vehicle_list = film_info["vehicles"]
            add_url_rows('Vehicle', film.id, vehicle_list)

        session.commit()


def main():
    create_tabls()
    init_data_of_tables()


if __name__ == '__main__':
    main()
