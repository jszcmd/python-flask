from flask import *

# 文件与目录的操作
import os
# 导入路径处理模块
from pathlib import Path

"""
要求:用户上传文件之后,我们需要在服务器内进行一个存储,服务器内专门开辟一个空间,让用户来上传图片,
下一次用户在不同的设备进行登录的时候,从服务器里面把图片拉下来,作为一个显示给用户看,
我们已经准备了一个名字为static文件夹,专门用来存放静态资源:1.可以让用户进行访问;
"""
'''
1.用户点击上传按钮(<input type="submit" value="上传">)以后,把他本地的文件进行上传;
2.我们在这里@app.route('/upload')做好接受,处理好以后放入到静态资源的文件夹里面;
3.然后把我们得到的当前文件的地址(static文件夹里面的地址),返回给前端的(<img src="" alt="">)页面
4.让它(<img src="" alt="">)做一个回显,显示出来他刚刚上传的那张图
'''
app = Flask(__name__)

# 用于闪现消息
app.secret_key = 'djavn14h55jdncvjaj5122'

# 配置上传文件的大小:防止用户随意上传内存过大的文件
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 也就是16MB的图片

"""生成唯一字符串,防止上传图片的覆盖,注意如果要下面的某种方法,要把它写到视图函数里面"""

'''方法1:'''
# 导入uuid用于生成唯一的字符串
import uuid
unique_string1 = str(uuid.uuid4()).replace('-','')
print('unique_string1',unique_string1)

'''方法2:'''
# 时间戳加上随机数
import time
import random

unique_string2 = str(time.time()).replace('.','')+str(random.randint(0,10000))
print('unique_string2:',unique_string2)

'''方法3:'''
# 用 hashlib+time生成随机字符串
import hashlib
unique_string3 = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
print('unique_string3:',unique_string3)

'''方法4:'''
# os模块,生成合适的随机字符串
import base64
import os

unique_string4 = base64.b64encode(os.urandom(6)).decode('utf-8')
print('unique_string4:',unique_string4)

@app.route('/')
def home():
    return render_template('uploads.html')

# 处理文件上传的路由
@app.route('/upload', methods=['POST'])
def upload_file():
    # 先看一看用户有没有进入到我们对应的区间
    # print('你进来喝王老吉') # 你进来喝王老吉
    # 证明:我们的用户提交的时候是触发了我们接受用户传递值的这个路由的(@app.route('/upload')

    # print(request.files)
    # 没有传递任何文件,打印的结果
    # ImmutableMultiDict([('file', <FileStorage: '' ('application/octet-stream')>)])
    # <FileStorage: ''  : 文件名其实是为空的数据

    # 判断是否有文件信息,如果没有文件就保留在当前页面
    if 'file' not in request.files:
        # 没有文件,就留在上传文件的这个上传页面,重定向到@app.route('/')
        # return redirect('/') # 可以直接这样,但是不太安全
        """
        如果前端页面没有file属性传递过来,则返回到文件上传页面
        也就是说,如果把<input type="file" name="file">这个删除掉,
        前端只会有一个"上传"的按钮,怎么点击都没有用,一直都是home这个页面
        """

        # 加上一个闪现消息,告诉用户没有file属性
        flash('啥也没有')

        return redirect(url_for('home'))

    # 接受传递过来的文件
    file = request.files['file']
    # print(file)
    # <FileStorage: '01.png' ('image/png')>

    # print(file.filename) # filename是filel里面的一个内置属性
    # 01.png  ---> 上传的文件名

    # 判断文件名不为空
    if file.filename == '':
        '''设置一个闪现消息给用户一个没有传递文件的提示'''
        flash('没有选择文件哦') # 把这个发送到前端来显示
        # 还是返回到上传页面
        return redirect(url_for('home'))

    # 用户提交了图片
    if file:
        # 获取文件名
        filename = file.filename

        # 获取文件的后缀名
        suffix = Path(file.filename).suffix
        # print(suffix)
        # .png 后缀名

        # 生成一个唯一的字符串防止重名,并且拼接上获取到的后缀名
        unique_string = str(uuid.uuid4()).replace('-','')
        # .replace('-','')把-替换掉,使用repalce

        # 文件保存的路径和文件名
        # file_path = os.path.join('static', filename)
        # 保存的文件名:用户上传的文件的文件名
        # 保存的路径:static.filename
        '''修改以后'''
        file_path = os.path.join('static',unique_string+suffix)
        # 以用户上传的文件名,存储到静态资源文件夹static中
        file.save(file_path)

        """到目前为止,我们已经完成了前两步;我们要进行回显"""

        # 设置闪现消息
        flash({'status':1,'url':unique_string+suffix})

        # 重定向到上传表单的页面,但是需要显示上传成功的消息 ---> 就需要到消息闪现
        return redirect(url_for('home'))

    """如果每一次都上传同一个文件名,这样就会覆盖"""

    return '你没有传递任何文件哦~'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)