from flask import Flask, request, render_template
import APP.views.handleMsg
from APP.control.admin import admin_handle
from APP.control.user import user_handle

app = Flask(__name__)


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


# 管理员添加大模型
@app.route('/admin/add_AI.html', methods=['GET', 'POST'])
def add_AI():
    return render_template('/admin/add_AI.html')


# 管理员信息页面
@app.route('/admin/admin_msg.html', methods=['GET', 'POST'])
def admin_msg():
    return render_template('/admin/admin_msg.html')


# 获取用户信息页面
@app.route('/admin/get_user_List', methods=['GET', 'POST'])
def get_user_List():
    if request.method == 'POST':
        print(admin_handle.get_users())
        return admin_handle.get_users()


# 获取所有大模型
@app.route('/admin/get_AI_list', methods=['POST'])
def get_AI_list():
    if request.method == 'POST':
        return admin_handle.get_AI()


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
def getMsg():
    data = request.get_data()
    if request.method == 'POST':
        handleMsg = APP.views.handleMsg.AIResponse(data)
        return handleMsg


if __name__ == '__main__':
    app.run()
