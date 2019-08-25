from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# 跨域访问
CORS(app)


@app.route('/')
def hello_world():
    return {
        "employees": [{
            "firstImg": "./02.png",
            "feature": "精巧玲珑",
            "price": "￥259",
            "weight": "107g",
            "size": "67x67x105mm",
            "contro_lens": "不可控",
            "v_resolution": "1280X720",
            "network": "不支持"

        }, {
            "firstImg": "./03.png",
            "feature": "精巧玲珑",
            "price": "￥259",
            "weight": "107g",
            "size": "67x67x105mm",
            "contro_lens": "不可控",
            "v_resolution": "1280X720",
            "network": "不支持"
        },
            {
                "firstImg": "./04.png",
                "feature": "精巧玲珑",
                "price": "￥259",
                "weight": "107g",
                "size": "67x67x105mm",
                "contro_lens": "不可控",
                "v_resolution": "1280X720",
                "network": "不支持"
            },
            {
                "firstImg": "./05.png",
                "feature": "精巧玲珑",
                "price": "￥259",
                "weight": "107g",
                "size": "67x67x105mm",
                "contro_lens": "不可控",
                "v_resolution": "1280X720",
                "network": "不支持"
            },
            {
                "firstImg": "./06.png",
                "feature": "精巧玲珑",
                "price": "￥259",
                "weight": "107g",
                "size": "67x67x105mm",
                "contro_lens": "不可控",
                "v_resolution": "1280X720",
                "network": "不支持"
            },
            {
                "firstImg": "./07.png",
                "feature": "精巧玲珑",
                "price": "￥259",
                "weight": "107g",
                "size": "67x67x105mm",
                "contro_lens": "不可控",
                "v_resolution": "1280X720",
                "network": "不支持"
            }
        ]
    }


if __name__ == '__main__':
    app.debug = True
    app.run()
