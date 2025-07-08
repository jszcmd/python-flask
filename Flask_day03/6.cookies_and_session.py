import os
from datetime import timedelta
from flask import *
app = Flask(__name__)

"""设定session的超时时间"""
session.permanent = True
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def index():
    return 'ok'

"""1.设置cookies"""
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('设置cookie')
    # 像浏览器写入一个key为name,值为python的cookie缓存,超时时间时6秒
    resp.set_cookie('name','python',max_age=3600)
    return resp
"""cookies的作用范围是当前服务器在整个区域名"""

"""2.获取cookies"""
@app.route('/get_cookie')
def get_cookie():
    # 获取cookie
    my_cookie = request.cookies.get('name')
    # 如果尝试获取cookies中没有的key值,返回的是None
    my_cookie1 = request.cookies.get('abc')
    # 如果获取不到,给它返回一个默认值default
    my_cookie2 = request.cookies.get('abcd','default')

    return f'获取到的cookies是{my_cookie}'

"""3.删除cookie"""
@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('删除cookie')
    # 删除key为name的cookie
    resp.delete_cookie('name')
    return resp


print("===================================================")

"""1.设置session"""
# 设置session需要一个唯一的字符串
app.config['SECRET_KEY'] = 'kdvj22advnd20jjhvb1adui2'
# app.config['SESSION_TYPE'] = os.urandom(24)
@app.route("/set_session")
def set_session():
    # 设置session
    session['name'] = 'wlj'
    session['age'] = '100'
    session['password'] = '123456'
    return 'session'

"""2.获取session"""
@app.route("/get_session")
def get_session():
    name = session.get('name')
    age = session.get('age')
    password = session.get('password')
    '''如果使用get即使属性不存在,也不会返回None'''
    return f'name:{name}, age:{age},password: {password}'


"""3.删除session"""
@app.route("/delete_session")
def delete_session():

    '''一个一个删除'''
    # 删除session的某一个值,返回删除的session值,如果没有该属性,返回None
    res = session.pop('name',None)
    # return f'删除的session:{res}' # 删除的session:wlj

    '''全部删除'''
    session.clear()

    return 'ok'

"""设定session的超时时间"""


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)