from flask import Flask, render_template

from werkzeug.routing import BaseConverter

app = Flask(__name__)

@app.route('/')
def home():
    return '我是首页'

print("=================================================================================")
""" 1.动态路由就是在路由地址后面传递参数,传递的参数,是可以变的,所以叫做动态路由 """
# 动态路由基础使用,动态路由可以动态的接受前端传递来的数据
@app.route('/param/<name>')  # '/param是路由地址,/<name>是传递的参数,是可以变的,所以叫做动态路由'
def get_url_param(name):
    return '传递过来的参数是:%s'%name
# 访问:http://127.0.0.1:8088/param/alex 结果:传递过来的参数是:alex

print("=================================================================================")
""" 2.动态路由可以约束参数的数据类型 """

# 约束传递的参数为整数
@app.route('/param_int/<int:id>')
def get_url_param_int(id):
    return '传递过来的整型的参数是:%s'%id

# 如果只是单单的@app.route('/param_int/<id>'),没有对id的数据类型进行约束
# 访问:http://127.0.0.1:8088/param_int/a 结果:传递过来的整型的参数是:a

# 约束传递的参数为浮点型
@app.route('/param_float/<float:fl>')
def get_url_param_float(fl):
    return '传递过来的浮点型的参数是:%s'%fl

# 如果访问:http://127.0.0.1:8088/param_float/123 结果:Not Found
# 访问:http://127.0.0.1:8088/param_float/123.02 结果:传递过来的整型的参数是:123.02

print("=================================================================================")
""" 3.动态路由可以约束参数的数据类型 """
# 如果只是单单的@app.route('/param_path/<p>')
# 访问:http://127.0.0.1:8088/param_path/123  结果:传递过来的参数是:123
# 但是万一我们在后面不小心补上了一个斜杠/,就出问题了
# 访问:http://127.0.0.1:8088/param_path/123/  结果:Not Found

# 匹配参数后面带 /
@app.route('/param_path/<path:p>')
def get_url_param_path(p):
    return '传递过来的参数是:%s'%p

# 访问:http://127.0.0.1:8088/param_path/666/  结果:传递过来的参数是:666/

print("=================================================================================")
""" 4.自定义正则的转化器 """
# 如果python自带的内容,自带的约束已经不能满足你的需求了,那我们可以给它定义一个正则转化器给它进行约束

# 重写
class RegexConverter(BaseConverter):
    def __init__(self,url_map,*items):
        super(RegexConverter,self).__init__(url_map)
        self.regex = r'\d+(,\d+)*' # 匹配1,2,3 这种数字列表
        self.num_args = 1

    def to_python(self,value:str):
        return value.split(',') if value else []

    def to_url(self,values):
        return ','.join(str(v) for v in values) if values else ''

# 注册reg的转换器
app.url_map.converters['re'] = RegexConverter

@app.route('/param_re/<re("\d"):num>/<re(\d+):num2>')
def get_param_re(num,num2):
    return '自定义正则转化器获取的参数:%s %s'%(num,num2)

# 访问:http://127.0.0.1:8088/param_re/1/777 结果:自定义正则转化器获取的参数:['1'] ['777']

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)


"""
上面是通过数据类型(已经知道了数据类型) -->(约束)参数
如果是传递了参数,怎么让前端显示它的数据类型,让电脑自动补充它的数据类型
"""


