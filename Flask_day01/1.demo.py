"""
Flask_Day01_:
一：Flask是一种类似于Django的框架：首先创建一个Flask项目：(在图片1中：)
1.可以直接用下面的创建一个Flask项目,但是可能会存在一些版本依赖的问题,如Debug的热更新就可能用不了，
你的Debug就可能无法进行调试，可能会有一直都是一个关闭的状态，怎么调都调不好--->不太推荐
2.直接创建一个纯Python项目 --->推荐

二：下载Flask包:
这边推荐直接在终端用：pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple flask
在图片2中：
Jinja2是一个模板文件，在Django里面的时候其实也用过，用过它类似的一些东西

四：配置
django中配置默认DEBUG=True,也就是我们修改这个文件里面的内容不需要重启服务器,而Flask需要自己设置DEBUG=True
修改DEBUG=True的三个方法：
    方法一：使用外部配置文件的形式(创建一个配置文件config.cfg:里面写上DEBUG = True)
        app.config.from_pyfile('config.cfg')
    方法二：配置类的形式
        class Config(object):
            DEBUG = True
        app.config.from_object(Config)
    方法三：app.run(debug=True)
"""
# 导入flask类
from flask import Flask, render_template, request, redirect

# flask 接受__name__,当前模块的文件名
app = Flask(__name__,static_folder='static',template_folder='templates') # 创建一个实例化对象
# 然后在左边Flask_day01下面创建一个名为static(用来存放静态资源),如果你想用它来存放图片也可以起名为image,
# 如果里面的static_folder='abc',则左边的文件目录名也要命名为abc,
# 一个名为templates的目录
'''我们也可以直接app = Flask(__name__),不用直接指定文件夹名,只要创建好static,templates就可以了'''
'''如果我们在static中放入图片(03.png图片名)：可以通过访问http://127.0.0.1:5000/static/4.png,看到图片'''

# 方法1：使用外部配置文件的形式
app.config.from_pyfile('config.cfg')
# 方法2：配置类的形式
class Config(object):
    DEBUG = True
# 从配置对象中进行查找
app.config.from_object(Config)


'''访问一下根路径'''
# 访问：http://127.0.0.1:5000/ 最后面的一个/加不加都可以
# 装饰器将路由映射到视图方法中
@app.route('/')
def index():
    return '爱喝王老吉'

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8088)
    # host:在同一个局域网内就可以通过访问你的本机的ip地址,访问到你的服务,port:设置端口号
    # 怎么查看自己的ip地址：win+R:cmd >>ipconfig