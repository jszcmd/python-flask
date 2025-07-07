from flask import Flask, render_template, request, redirect
app = Flask(__name__)

"""requests对象中有哪些属性"""
"""form,args,values,cookies,headers,method,files"""

# 用户访问根目录的时候,限制它的请求方式只有GET POST
@app.route('/', methods=['GET', 'POST'])
def index():

    """1.headers"""
    '''
    请求头存为一个类似字典的对象,通常前端会携带token值进行请求 
    token:用户登录以后的唯一标识       类型:dict
    '''
    # print(request.headers)

    print("=================================================================")
    """2.form属性"""
    '''
    功能:一个包含解析过的从POST或PUT请求发送的表单对象的MultiDict
    注意:上传文件不会在这里,而是在files属性中    类型:MultiDict
    '''
    # 获取form表单,获取post提交的数据
    # post_dict = request.form
    # print(post_dict)
    # 在Apipost 软件中用:先选择提交方式post提交,在选中body,选中form_data
    # 传递参数: name:王老吉  age:100  color:red
    # 访问:http://127.0.0.1:8088 结果:Hello World!
    # print(post_dict)打印的结果
    # ImmutableMultiDict([('name', '王老吉'), ('age', '100'), ('color', 'red')])

    print("=================================================================")
    """3.args属性"""
    '''
    功能:一个包含解析过的查询字符串(其实就是 ?问号后面的参数值)
    也就是说:可以用args来接收get方式的参数传递 类型:MultiDict
    '''
    # args查询字符串 url ?后面的参数
    query_dict = request.args
    # print(query_dict)
    # 1.Apipost:使用get请求,选中query
    # 2.直接访问:http://127.0.0.1:8088/?name=jack&age=18
    # query_dict 打印的结果:
    # ImmutableMultiDict([('name', 'jack'), ('age', '18')])

    print("=================================================================")
    """4.values属性"""
    '''包含了form和args全部内容,可以方便快速的用它获取到get或者post请求传递过来的值'''
    # 获取所有的查询参数和post参数
    # all_dict = request.values
    # print(all_dict)

    # 发送get请求:
    # CombinedMultiDict([ImmutableMultiDict([('a', '2333')])])

    # 发送post请求:
    # 访问:http://127.0.0.1:8088?a=2333 结果:Hello World!
    # CombinedMultiDict([ImmutableMultiDict([('a', '2333')]), ImmutableMultiDict([('name', '小甜水'), ('age', '100'), ('color', 'red')])])
    # CombinedMultiDict([ImmutableMultiDict([('a', '2333')]) get请求
    # ImmutableMultiDict([('name', '小甜水'), ('age', '100'), ('color', 'red')])]) post请求
    # 同时get和post请求

    print("=================================================================")
    """5.cookies属性"""
    '''包含请求中传递的所有cookie内容 类型:dict'''
    # # 获取cookie
    # 首先在浏览器里设置一个cookies name:王老吉
    # cookie = request.cookies
    # print(cookie)
    # ImmutableMultiDict([('name', 'ç\x8e\x8bè\x80\x81å\x90\x89')])

    print("=================================================================")
    # 获取某个参数值的get方法,如果不存在这个key会报错,为了不报错可以传递一个默认值,如果不存在key,将使用默认值
    # 如果是多个值,使用getlist方法,如果不存在,则返回空列表
    # 使用get设置默认值
    # a = query_dict.get('aaa')
    # print(a)
    # 访问:http://127.0.0.1:8088/?name=jack&age=18 结果:Hello World!
    # print(a)打印结果:None

    # 使用get设置默认值
    # a = query_dict.get('aaa',' ')
    # print('hello:',a)
    # 访问:http://127.0.0.1:8088/?name=jack&age=18 结果:Hello World!
    # print('hello:',a)打印结果:hello:

    a = query_dict.getlist('bbb')
    print(a) # []

    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)
