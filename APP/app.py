import json
from urllib.parse import unquote, parse_qs
from flask import Flask, request, render_template
import APP.views.handleMsg
from APP.control.user import user_handle
from APP.model.entity.User import User

app = Flask(__name__)


# 用户登录
@app.route('/user/login.html', methods=['GET', 'POST'])
def user_login(name=None):
    return render_template('user/login.html')


# 管理员登录
@app.route('/admin/admin_login.html', methods=['GET', 'POST'])
def admin_login(name=None):
    return render_template('/admin/admin_login.html')


# 用户注册
@app.route('/user/user_register.html', methods=['GET', 'POST'])
def user_register(name=None):
    return render_template('/user/user_register.html')


@app.route('/getMsg', methods=['POST'])
def getMsg(msg=None):
    data = request.get_data()
    if request.method == 'POST':
        handleMsg = APP.views.handleMsg.AIResponse(data)
        return handleMsg


@app.route('/user_register_check', methods=['GET', 'POST'])
def user_register_check():
    print(request.method)
    if request.method == 'POST':
        decoded_data = request.data.decode('utf-8')
        # 解析查询字符串
        parsed_data = parse_qs(decoded_data)
        # 获取属性值
        username = parsed_data['username'][0]
        email = unquote(parsed_data['email'][0])
        password = parsed_data['password'][0]
        new_user = User(username=username, password=password, email=email)
        msg, status = user_handle.user_register_check(new_user)
        if status:
            status = 1
        else:
            status = 0
        ret_msg = {'msg': msg, 'status': status}
        return json.dumps(ret_msg)


@app.route('/user_login_check', methods=['GET', 'POST'])
def user_register_check2():
    if request.method == 'POST':
        decoded_data = request.data.decode('utf-8')
        # 解析查询字符串
        parsed_data = parse_qs(decoded_data)
        # 获取属性值
        username = parsed_data['username'][0]
        password = parsed_data['password'][0]
        new_user = User(username=username, password=password)
        msg, status = user_handle.user_login_check(new_user)
        if status:
            status = 1
        else:
            status = 0
        ret_msg = {'msg': msg, 'status': status}
        return json.dumps(ret_msg)


if __name__ == '__main__':
    app.run()
