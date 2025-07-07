from flask import Flask, render_template, request, redirect
app = Flask(__name__)

"""1.装饰器将路由映射到视图函数中"""
@app.route('/')
def index():
    '''查看路由信息'''
    # print(app.url_map)
    return 'Hello World!'

# Map([<Rule '/static/<filename>' (HEAD, GET, OPTIONS) -> static>,
#  <Rule '/' (HEAD, GET, OPTIONS) -> index>,
#  <Rule '/route' (HEAD, GET, OPTIONS) -> index>,
#  <Rule '/home' (HEAD, GET, OPTIONS) -> home>])

@app.route('/home')
def home():
    return '我是首页'


"""2.方法调用的形式:"""
# 前面的index就是你要注册规则的名称,默认也是视图函数的名字,
# 后面的index对应的url的处理函数,是视图函数,两个通常写的是一样的
app.add_url_rule('/route','index',view_func=index)



'''问题：一个函数能被多个视图函数使用吗?'''
# 访问：http://127.0.0.1:5000/route 得到的也是：Hello World!
'''答案：可以'''


print("=================================================================================")
"""案例2：同一个路由装饰不同视图函数,只有第一个视图函数会匹配到 """

@app.route('/index')
def index1():
    print(app.url_map)
    return '我是第一个index'

# print(app.url_map)的结果：
# Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
#  <Rule '/index' (HEAD, OPTIONS, GET) -> index1>,
#  <Rule '/index' (HEAD, OPTIONS, GET) -> index2>])
"""
访问：http://127.0.0.1:5000/index,结果：我是第一个index
说明路由'/index'匹配到的是第一个视图函数def index1(),
但是上面为什么两个映射都有???
"""

@app.route('/index')
def index2():
    # print(app.url_map),这个print是不会执行的
    return '我是第二个index'

# 访问：http://127.0.0.1:5000/index 结果：我是第一个index
# 并不是第二个覆盖第一个,而是匹配到第一个
"""同一个路由装饰不同视图函数,只有第一个视图函数会匹配到"""


print("=================================================================================")
"""案例3：一个视图函数有多个路由装饰器呢? """

@app.route('/details1')
@app.route('/details2')
def detail():
    print(app.url_map)
    return '我是详情页'

# 访问：http://127.0.0.1:5000/details1 结果：我是详情页
# 访问：http://127.0.0.1:5000/details2 结果：我是详情页

# print(app.url_map)打印的结果：
# Map([<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
#  <Rule '/details2' (HEAD, OPTIONS, GET) -> detail>,
#  <Rule '/details1' (HEAD, OPTIONS, GET) -> detail>])



if __name__ == '__main__':
    app.run(debug=True)