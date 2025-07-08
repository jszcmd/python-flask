import json

from flask import Flask, jsonify, request,make_response
app = Flask(__name__)

"""返回json数据"""

# 返回的中文值有问题时设置
app.config['JSON_AS_ASCII'] = False

'''方法1:手动添加,使用json模块中json.dumps()函数'''
@app.route('/')
def index():

    data = {'id': 1, 'name': 'jack','age':18}
    response = make_response(json.dumps(data),200)

    # 一定要把这个改成json数据格式
    response.headers['Content-Type'] = 'application/json'
    return response

'''方法2:使用flask中内置的jsonify'''
@app.route('/json')
def return_json():
    data = {'code': 200, 'msg': 'success,成功', 'data':[{'id': 1, 'name': 'jack', 'age':18}]}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=8088)