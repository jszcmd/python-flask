from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():

    # return 'ok'
    # 访问:http://127.0.0.1:8088?name=jack&age=18 结果:ok

    # 简单粗暴使用values
    v_dict = request.values

    # 可以在这里处理数据,然后再返回出去
    data = v_dict.get('data','')

    return v_dict
    # 访问:http://127.0.0.1:8088?name=jack&age=18
    # {                 前端返回json对象
    # 	"age": "18",
    # 	"name": "jack"
    # }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)