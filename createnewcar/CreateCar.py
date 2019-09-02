from flask import Flask
from flask_cors import CORS

from view import create

app = Flask(__name__)
# 跨域访问
CORS(app)


@app.route('/', methods=['POST'])
def new_car():
    return create()


if __name__ == '__main__':
    app.debug = True
    app.run()
