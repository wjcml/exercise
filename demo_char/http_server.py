#!/usr/bin/env python3
from flask import Flask, render_template, request, escape, json
from flask import jsonify
import hashlib

import base64
import mysql.connector

app = Flask(__name__)

# 不使用 ascii 编码来序列化JSON对象
# 显示中文
app.config['JSON_AS_ASCII'] = False

dbconfig = {
                'host': '127.0.0.1',
                'user': 'root',
                'password': '123456',
                'database': 'test'
            }


@app.route("/", methods=["GET"])
def hello():
    with open("./static/logo.jpg", "rb") as f:
        # b64encode是编码，b64decode是解码
        base64_data = base64.b64encode(f.read())
        try:
            conn = mysql.connector.connect(**dbconfig)
            cursor = conn.cursor()

            _SQL = "insert into tb_img(img) values(%s)"

            cursor.execute(_SQL, (base64_data, ))

            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)

        return "success"


@app.route("/img", methods=['GET'])
def api():
    try:
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()

        _SQL = "select * from tb_img"

        cursor.execute(_SQL)
        result = []
        for img in cursor.fetchall():
            result.append(img[1])

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    return render_template("index.html", result=result)


@app.route("/to-ascii", methods=["GET"])
def to_ascii():
    a = [67, 68, 71, 69, 69, 75, 65, 77, 80]
    result = []
    for s in a:
        result.append(chr(s))
    return jsonify("".join(result))


@app.route("/to-sha256")
def to_sha256():
    data = {
            "advantage": ["五险一金", "团建"],
            "companyMainPage": "https://www.lagou.com/gongsi/420697.html",
            "companyName": "成都玛尔斯科技有限公司",
            "companyNature": ["移动互联网", "社交"],
            "edu": "本科及以上",
            "exp": "经验3-5年",
            "hrName": "黄小姐",
            "hrPosition": "招聘专员",
            "location": "成都",
            "salary": "14k-18k",
            "position": "Python开发工程师",
            "scale": "15-50人",
            "stage": "未融资",
            "tagList": ["证券/期货", "基金", "Python", "MySQL", "区块链", "前端开发"],
            "publishTime": "2019-09-28 17:00:10",
            "spiderUuid": "afe737ef-2e14-472e-80d7-af9f9f8c5cab"
            }
    data_json = json.dumps(data, encoding="utf-8")
    sha256 = hashlib.sha256()
    sha256.update(data_json)
    res = sha256.hexdigest()
    print("sha256加密结果:", res)
    return res


if __name__ == '__main__':
    app.debug = True
    app.run()
