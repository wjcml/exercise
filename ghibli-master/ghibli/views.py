#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import inspect

from common import session
from common import hlog
from model import Film, Locations
from flask import request, flash


def get_film_list():
    """
    获取电影信息
    :return:
    """

    from utils import get_urls

    func_name = inspect.stack()[0][3]
    hlog.enter_func(func_name)

    film_list = list()
    film_objs = session.query(Film).all()

    for obj in film_objs:
        film_id = obj.id
        hlog.var('film_id', film_id)

        location_list = get_urls('Location', film_id)
        people_list = get_urls('People', film_id)
        specie_list = get_urls('Specie', film_id)
        vehicle_list = get_urls('Vehicle', film_id)

        film = {
            "id": obj.id,
            "title": obj.title,
            "description": obj.description,
            "director": obj.director,
            "producer": obj.producer,
            "release_date": obj.release_date,
            "rt_score": obj.rt_score,
            "url": obj.url,
            "people": people_list,
            "species": specie_list,
            "locations": location_list,
            "vehicles": vehicle_list
        }

        film_list.append(film)

    hlog.info("读取电影信息成功。")
    hlog.exit_func(func_name)

    return film_list


def add_film():
    _id = request.form.get('id')
    _title = request.form.get('title')
    _description = request.form.get('description')
    _director = request.form.get('director')
    _producer = request.form.get('producer')
    _release_date = request.form.get('release_date')
    _rt_score = request.form.get('rt_score')
    _url = request.form.get('url')
    location = request.form.get('location')

    hlog.var('_id', _id)
    hlog.var('_title', _title)
    hlog.var('_description', _description)
    hlog.var('_director', _director)
    hlog.var('_producer', _producer)
    hlog.var('_release_date', _release_date)
    hlog.var('_rt_score', _rt_score)
    hlog.var('_url', _url)
    hlog.var('location', location)

    old_film = session.query(Film).filter(Film.id == _id).all()

    if old_film:
        return {"status": "1", "message": "电影编号已经存在"}

    film = Film(id=_id,
                title=_title,
                description=_description,
                director=_director,
                producer=_producer,
                release_date=_release_date,
                rt_score=_rt_score,
                url=_url
                )
    session.add(film)

    loc = Locations(film_id=_id, url=location)
    session.add(loc)

    session.commit()

    return {"status": "0", "message": "新增成功"}


def delete_film():
    _id = request.form.get('id')

    if _id:
        film = session.query(Film).filter(Film.id == _id).delete()
        session.commit()
        return {"status": "0", "message": "电影 " + _id + " 删除成功"}

    return {"status": "1", "message": "电影编号无效"}


def get_film_info(film_id):
    # film_id = request.args.get('id')

    if film_id:
        films = session.query(Film).filter(Film.id == film_id).first()
        locations = session.query(Film).filter(Film.id == film_id).all()

        if films:
            return films, locations

    return Film()


def add_location():
    try:
        film_id = request.form.get('film_id')
        location = request.form.get('location')

        if not film_id:
            return {"code": False, "message": "添加失败，请输入电影编号"}

        film = session.query(Film).filter(Film.id == film_id).all()
        if not film:
            return {"code": False, "message": "添加失败，没有此电影"}

        if not location:
            return {"code": False, "message": "添加失败，location不能为空"}

        loc = Locations(film_id=film_id, url=location)
        session.add(loc)
        session.commit()

        return {"code": True, "message": "添加成功"}
    except Exception as e:
        print(e)
        return {"code": False, "message": "出错啦，添加失败"}
