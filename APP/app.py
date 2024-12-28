import os
from datetime import timedelta

from flask import Flask, request, render_template
from APP.control.AI_model import AI_ask_handle
from APP.control.admin import admin_handle
from APP.control.user import user_handle
from flask import session

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)
online_user = {}


# 管理员
# 管理员登录
@app.route('/admin/admin_login.html', methods=['GET', 'POST'])
def admin_login():
    return render_template('/admin/admin_login.html')


# 管理员主页面
@app.route('/admin/admin_main.html', methods=['GET', 'POST'])
def admin_main_passage():
    return render_template('/admin/admin_main.html')


# 管理员登录判断
@app.route('/admin_login_check', methods=['GET', 'POST'])
def admin_login_check():
    if request.method == 'POST':
        ret_msg = admin_handle.login_check(request)
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
@app.route('/get_user_info', methods=['GET', 'POST'])
def get_user_info():
    if request.method == 'POST':
        return admin_handle.get_users()


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
@app.route('/user_register_check', methods=['GET', 'POST'])
def user_register_check():
    if request.method == 'POST':
        ret_msg = user_handle.register_check(request)
        return ret_msg


# 用户登录判断
@app.route('/user_login_check', methods=['GET', 'POST'])
def user_login_check():
    if request.method == 'POST':
        ret_msg = user_handle.login_check(request)
        return ret_msg


# 用户登出
@app.route('/user_sign_out', methods=['GET', 'POST'])
def user_sign_out():
    user_id = session.get('user_id')
    if user_id:
        online_user.pop(str(user_id))
        return 'User {} has been logged out.'.format(user_id)
    else:
        return 'No user is logged in.'


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


# 大模型
@app.route('/AI_chat', methods=['POST'])
def AI_chat():
    if request.method == 'POST':
        return AI_ask_handle.get_user_msg(request)


# 获取模型
@app.route('/admin/get_AI_By_Id', methods=['GET', 'POST'])
def get_AI_By_Id():
    if request.method == 'POST':
        return admin_handle.get_model_by_id(request)


if __name__ == '__main__':
    app.run()
