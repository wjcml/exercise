#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
app.py 只负责访问入口相关的代码
"""

from flask import Flask, url_for
from flask import jsonify
from flask import render_template
from flask import redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')

# 不使用 ascii 编码来序列化JSON对象
# 显示中文
app.config['JSON_AS_ASCII'] = False


@app.route('/')
@app.route("/?<msg>", methods=["GET"])
def index(msg=None):
    return render_template('index.html', msg=msg)


@app.route("/add_film", methods=["GET"])
def add_html():
    return render_template('add.html')


@app.route("/get_film_list", methods=["GET"])
def films():
    from views import get_film_list

    return jsonify(get_film_list())


@app.route("/get_film_info/<film_id>", methods=["GET"])
def get_film_info(film_id):
    from views import get_film_info

    film, locations = get_film_info(film_id)

    return render_template('info.html', film=film, locations=locations)


@app.route("/delete_film", methods=["POST"])
def del_film():
    from views import delete_film

    result = delete_film()

    return redirect(url_for('index', msg=result))


@app.route("/add_film", methods=["POST"])
def add_film():
    from views import add_film

    result = add_film()

    return redirect(url_for('index', msg=result))


@app.route("/add_location", methods=["POST"])
def add_location():
    from views import add_location

    result = add_location()

    return redirect(url_for('index', msg=result))


if __name__ == '__main__':
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5000
    )
