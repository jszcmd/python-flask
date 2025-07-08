from flask import Flask,make_response,request
app = Flask(__name__)

@app.route('/')
def index():
    """第一个参数:响应体;
    第二个参数:响应的状态码;也可以是 666wlj
    第三个参数:参数响应头,可以是一个字典"""
    return '我爱喝王老吉','300',{'name':'jack','chapter':'Flask'}

@app.route('/make_response')
def make_response():
    # 创建一个响应的对象
    response = make_response('超爱喝加多宝')
    response.status_code = '300'
    # 不能传输中文
    response.headers['abc'] = 'python'

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)
