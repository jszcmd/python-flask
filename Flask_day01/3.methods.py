from flask import Flask,render_template,request,redirect,url_for,session
app = Flask(__name__)


print("=============================================================================")
""" 1.请求方式:methods可以设置当前路由的请求方式 """
# methods可以设置当前路由的请求方式
@app.route('/login',methods=['POST','GET'])
def index():
    print(app.url_map)
    if request.method == 'POST':
        return '你用post请求了我'
    else:
        return '这里是get请求'
# 访问：http://127.0.0.1:8088/login 结果：这里是get请求

# print(app.url_map)打印的结果:
# Map([<Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>,
#  <Rule '/login' (POST, HEAD, GET, OPTIONS) -> index>])

# 如果是把methods=['GET','POST']改成methods=['POST']
# 访问：http://127.0.0.1:8088/login 结果：Method Not Allowed

"""问题:用post怎么请求呢?"""
'''
方法1：使用templates创建一个form表格,<form action="" method="post" enctype="multipart/form-data">
方法2：使用软件工具Apipost(可用于接口调试)
'''

print("=============================================================================")
""" 2.反向解析:我们可以通过视图函数的名称去解析得到视图对应的url的地址 """
# 视图函数 ---> 路由url
@app.route('/python')
def req_python():
    return 'python'

@app.route('/url_for')
def req_url():
    return f'<a href="{url_for("req_python")}">链接</a>'

# 首先我们去访问:http://127.0.0.1:8088/url_for 结果：链接
# 然后点击"链接" 直接跳到:http://127.0.0.1:8088/python 结果:python

"""问题当多个路由装饰器修饰一个视图函数的时候,对这个视图函数反向解析,又会怎么样??"""
@app.route('/cpp')
@app.route('/java')
def req_code():
    return 'Hello world!!!'

@app.route('/url_for_code')
def req_url_for_code():
    return f'<a href="{url_for("req_code")}">链接</a>'

# 多个路由装饰器修饰一个视图函数的时候,对这个视图函数反向解析,又会怎么样???
# 用两个路由/cpp 和/java来修饰一个视图函数reg code(),结果跳转到了127.0.0.1:8088/iava




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)