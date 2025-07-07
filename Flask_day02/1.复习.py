from flask import Flask, render_template, request, redirect
app = Flask(__name__)

"""1.用路由装饰器装饰视图函数函数"""
@app.route('/')
def index():
    return '我是初始页面'
# 这种方式默认把路由映射表里面的名称和视图名保持一致

"""2.同一个路由装饰不同视图函数,只有第一个视图函数会匹配到"""
@app.route('/home')
def home1():
    print(app.url_map)
    return '我是首页111'

@app.route('/home')
def home2():
    return '我是首页222'

# print(app.url_map) 打印出来的结果:
# Map([<Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>,
#  <Rule '/' (HEAD, GET, OPTIONS) -> index>,
#  <Rule '/home' (HEAD, GET, OPTIONS) -> home1>,
#  <Rule '/home' (HEAD, GET, OPTIONS) -> home2>,
#  <Rule '/www' (HEAD, GET, OPTIONS) -> 王老吉>,
#  <Rule '/param/<id>' (HEAD, GET, OPTIONS) -> get_id>])
"""3.使用函数调用的形式"""
# 第一个参数(param1):要访问的路由地址;
# 第二个参数(param2):写入到路由注册表里面的名称;
# 第三个参数(param3):执行的视图函数.

def wlj():
    print(app.url_map)
    return 'Hello World!'
app.add_url_rule('/www','王老吉',view_func=wlj)

"""4.动态路由"""
# 访问:http://127.0.0.1:8088/param/133 结果:123
# restful API风格:省略了像传统的一些 ?形式的传参,以斜杠(/)来连接每一个参数
# 参数的名称从哪里来? 后台去进行处理,前端只管去传递参数

@app.route('/param/<int:id>')
def get_id(id):
    return id

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)