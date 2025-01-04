import json
import secrets
import string
from datetime import timedelta

from flask import Flask, request, render_template, redirect, url_for
from APP.control.AI_model import AI_ask_handle
from APP.control.admin import admin_handle
from APP.control.user import user_handle
from flask import session


def generate_secret_key(length=32):
    """
    使用secrets模块生成指定长度的SECRET_KEY
    """
    print("generate secret key")
    alphabet = string.ascii_letters + string.digits
    print(''.join(secrets.choice(alphabet) for _ in range(length)))
    return ''.join(secrets.choice(alphabet) for _ in range(length))
app = Flask(__name__)
app.secret_key = "114514"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
online_users = {}
app.config["SESSION_TYPE"] = 'filesystem'

# 管理员
# 管理员登录
@app.route('/admin_login.html', methods=['GET', 'POST'])
def admin_login():
    return render_template('/admin/admin_login.html')


# 管理员主页面
@app.route('/admin/admin_main.html', methods=['GET', 'POST'])
def admin_main_passage():
    return render_template('/admin/admin_main.html')


# 管理员登录判断
@app.route('/admin_login_check', methods=['GET', 'POST'])
def admin_login_check():
    global online_users
    if request.method == 'POST':
        ret_msg = admin_handle.login_check(request,online_users)
        return ret_msg


# 管理员管理用户页面
@app.route('/admin/manage_user.html', methods=['GET', 'POST'])
def manage_user():
    return render_template('/admin/manage_user.html')


# 管理员管理大模型页面
@app.route('/admin/manage_ai.html', methods=['GET', 'POST'])
def manage_ai():
    return render_template('/admin/manage_AI.html')


# 管理员
@app.route('/admin/manage_web.html', methods=['GET', 'POST'])
def manage_web():
    return render_template('/admin/manage_web.html')


# 管理员添加大模型页面
@app.route('/admin/add_AI.html', methods=['GET', 'POST'])
def add_AI_passage():
    return render_template('/admin/add_AI.html')


# 管理员删除大模型
@app.route('/admin/delete_AI', methods=['GET', 'POST'])
def add_AI_delete():
    if request.method == 'POST':
        return admin_handle.model_delete(request)


# 管理员添加大模型页面
@app.route('/admin/add_AI', methods=['GET', 'POST'])
def add_AI():
    if request.method == 'POST':
        return admin_handle.model_add(request)


# 管理员信息页面
@app.route('/admin/admin_msg.html', methods=['GET', 'POST'])
def admin_msg():
    return render_template('/admin/admin_msg.html')


# 获取全部用户信息页面
@app.route('/admin/get_user_List', methods=['GET', 'POST'])
def get_user_List():
    if request.method == 'POST':
        return admin_handle.get_users()


# 获取用户信息页面
@app.route('/user/get_user_info', methods=['GET', 'POST'])
def get_user_info():
    if request.method == 'POST':
        return admin_handle.get_users()

@app.route('/user/get_user_by_name', methods=['GET', 'POST'])
def get_user_by_username():
    if request.method == 'POST':
        return admin_handle.get_user_by_username(request)

@app.route('/user/sign_in', methods=['GET', 'POST'])
def user_sign_in():
    if request.method == 'POST':
        return user_handle.user_sign_in(request)

# 获取所有大模型
@app.route('/admin/get_AI_list', methods=['POST'])
def get_AI_list():
    if request.method == 'POST':
        return admin_handle.get_AI()


# 用户升级
@app.route('/admin/user_update', methods=['POST'])
def user_update():
    if request.method == 'POST':
        return admin_handle.user_level_up(request)


# 用户删除
@app.route('/admin/user_delete', methods=['POST'])
def user_delete():
    if request.method == 'POST':
        return admin_handle.user_delete(request)


# 用户
# 用户登录
@app.route('/user/login.html', methods=['GET', 'POST'])
def user_login():
    return render_template('user/login.html')


# 用户注册
@app.route('/user/user_register.html', methods=['GET', 'POST'])
def user_register():
    return render_template('/user/user_register.html')


# 用户注册判断
@app.route('/user/user_register_check', methods=['GET', 'POST'])
def user_register_check():
    if request.method == 'POST':
        ret_msg = user_handle.register_check(request)
        return ret_msg


# 用户登录判断
@app.route('/user/user_login_check', methods=['GET', 'POST'])
def user_login_check():
    global online_users
    if request.method == 'POST':
        ret_msg = user_handle.login_check(request,online_users)
        return ret_msg


# 用户登出
@app.route('/user/user_sign_out', methods=['GET', 'POST'])
def user_sign_out():
    if request.method == 'POST':
        session_id = request.cookies.get('session')
        global online_users
        delete_session_id_to_user(session_id,0,online_users)
        msg,status = user_handle.user_sign_out(request)  # 将用户标记为离线
        if status:
            return render_template('user/login.html')
        else:
            ret_msg = {'data': msg, 'status': status}
            return json.dumps(ret_msg)


# 用户主页面
@app.route('/user/user_main.html', methods=['GET', 'POST'])
def user_main():
    return render_template('/user/user_main.html')


# 用户聊天页面
@app.route('/user/chat.html', methods=['GET', 'POST'])
def chat():
    return render_template('/user/chat.html')


# 用户信息页面
@app.route('/user/user_msg.html', methods=['GET', 'POST'])
def user_msg():
    return render_template('/user/user_msg.html')

# 管理员登出
@app.route('/admin/admin_sign_out', methods=['POST'])
def admin_sign_out():
    if request.method == 'POST':
        session_id = request.cookies.get('session')
        delete_session_id_to_user(session_id,1,online_users)
        return render_template('/admin/admin_login.html')

# 大模型
@app.route('/user/AI_chat', methods=['POST'])
def AI_chat():
    if request.method == 'POST':
        return AI_ask_handle.get_user_msg(request)


# 获取模型
@app.route('/admin/get_AI_By_Id', methods=['GET', 'POST'])
def get_AI_By_Id():
    if request.method == 'POST':
        return admin_handle.get_model_by_id(request)

def get_real_session_id(session_id):
    first_part = session_id.split('.')[0]
    return first_part

def set_session_id_to_user(session_id,status,online_users):
    if online_users.get(session_id) is None:
        online_users[session_id] = [0]*2
        online_users[session_id][status] = 1
    else:
        online_users[session_id][status] = 1

def get_session_id_to_user(session_id,status,online_users):
    if online_users.get(session_id) is None:
        return False
    return online_users.get(session_id)[status]==1

def delete_session_id_to_user(session_id, status, online_users):
    if online_users.get(session_id) is None:
        return False
    online_users[session_id][status] = 0

# 过滤器
@app.before_request
def before_admin_request():
    if request.path.startswith('/'):
        if session.get('get') is None:
            session['get'] = 1


@app.before_request
def before_user_request():
    if request.path.startswith('/user/login.html'):
        pass
    elif request.path.startswith('/user/user_register.html'):
        pass
    elif request.path.startswith('/user/user_register_check'):
        pass
    elif request.path.startswith('/user/user_login_check'):
        pass
    elif request.path.startswith('/user/'):
        return
        session_id = request.cookies.get('session')
        if get_session_id_to_user(session_id, 0, online_users) != 1:
            return """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>404 - 页面未找到</title>
    <link rel="stylesheet" href="{{ url_for('static', path='layui/css/layui.css') }}">
</head>

<body>
    <div class="layui-container">
        <div class="layui-row">
            <div class="layui-col-md12">
                <div class="layui-card">
                    <div class="layui-card-header">
                        <h2>请先登录账号后再查看</h2>
                    </div>
                    <div class="layui-card-body">
                        <p>很抱歉，您没有登录账户，无法查看</p>
                        <p>您可以尝试返回上一页或者去 <a href="{{ url_for('index') }}">首页</a> </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="{{ url_for('static', path='layui/layui.js') }}"></script>
</body>

</html>"""

def before_admin_request():
    if request.path.startswith('/admin/'):
        session_id= request.cookies.get('session')
        if get_session_id_to_user(session_id,1,online_users) !=1 :
            return """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>404 - 页面未找到</title>
     <link rel="stylesheet" href="../static/layui/css/layui.css" media="all">
    <script src="../static/js/jquery-3.5.1.js"></script>
    <script src="../static/layui/layui.js"></script>
</head>

<body>
    <div class="layui-container">
        <div class="layui-row">
            <div class="layui-col-md12">
                <div class="layui-card">
                    <div class="layui-card-header">
                        <h2>权限不足</h2>
                    </div>
                    <div class="layui-card-body">
                        <p>很抱歉，您的权限不足，无法查看</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="{{ url_for('static', path='layui/layui.js') }}"></script>
</body>

</html>"""


if __name__ == '__main__':
    app.run()
