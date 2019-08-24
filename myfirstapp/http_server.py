#!/usr/bin/env python3

from flask import Flask, render_template, request, escape
from flask import jsonify
from db_User import User, session
import hashlib

app = Flask(__name__)

# 不使用 ascii 编码来序列化JSON对象
# 显示中文
app.config['JSON_AS_ASCII'] = False


def get_user_info_from_db():
    """
    TODO 等待实现
    从MySQL数据库的 user 表中获取用户信息
    :return map: 返回用户信息字典
    """
    user = session.query(User).filter(User.id == 1).first()
    print(user)
    # 将user的信息存入字典user_info中
    user_info = dict()
    user_info['name'] = user.name
    user_info['age'] = user.age
    user_info['phone'] = user.phone

    return user_info

@app.route("/", methods=["GET"])
def hello():
    users = session.query(User).all()
    return render_template('index.html', title='添加数据', users=users)


@app.route("/api", methods=['GET'])
def api():
    return 'aa'


@app.route("/api/v2/getUserInfo", methods=["GET"])
def user_info():
    return jsonify(get_user_info_from_db())
    # get_user_info_from_db()


@app.route("/add", methods=['POST'])
def add_data():
	name = request.form['name']
	age = request.form['age']
	password = request.form['password']
	phone = request.form['phone']

	new_user = User(name=name, age=age, password=password, phone=phone)
	session.add(new_user)	# 添加到session
	session.commit()	# 提交保存到数据库

	users = session.query(User).all()

	return render_template("index.html", users = users)

if __name__ == '__main__':
    app.debug = True
    app.run()
