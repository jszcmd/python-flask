from flask import Flask, render_template,abort
app = Flask(__name__)


@app.route('/')
def index():
    return '我是首页'

@app.route('/error')
def my_error():
    # 使用abort手动抛出404错误
    abort(404) # 因为抛出错误以后,用户只能看到一串冰冷的报错信息,用户体验极差!!!
    # 如果使用abort(500),那么再访问/error,就会抛出系统错误的页面
    return 'error'

# 1.直接用浏览器访问:http://127.0.0.1:8088/error 结果:Not Found
# 2.用Apipost发送请求,访问:http://127.0.0.1:8088/error
# 结果:<!doctype html> --->这个就是404自带的页面
# <html  lang=en>
#     <title>404 Not Found</title>
#     <h1>Not Found</h1>
#     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>

# 如果把abort(404)去掉,
# 访问:http://127.0.0.1:8088/error 结果:error

"""自定义一个报错页面"""
# 错误装饰器,可以有多个errorhandler去处理不同的错误
@app.errorhandler(404)
def error_404(error):
    return render_template('404_error.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8088)