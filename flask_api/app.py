from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
# 跨域访问
CORS(app)


@app.route('/api/', methods=('GET',))
def get_data():
    """
    直接点击index.html文件，然后异步访问该地址
    :return: json对象data_list
    """
    try:
        data_list = []
        # 从index.txt中读取数据
        with open("./index.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                data = line.split(' ')
                # 将数据放到data_list中
                data_list.append({'title': data[0], 'intro': data[1]})
        # 返回json对象
        return jsonify(data_list)
    except Exception as e:
        print(e)
        return '出错啦'


if __name__ == '__main__':
    app.debug = True
    app.run()
