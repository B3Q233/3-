from flask import Flask, request, render_template
import APP.views.handleMsg

app = Flask(__name__)

# 用户登录
@app.route('/user/login.html', methods=['GET', 'POST'])
def user_login(name=None):
    if request.method == 'POST':
        print(request.headers)
        print(request.get_json())
        return "success"
    return render_template('user/login.html')

# 管理员登录
@app.route('/admin/admin_login.html', methods=['GET', 'POST'])
def admin_login(name=None):
    if request.method == 'POST':
        print(request.headers)
        print(request.get_json())
        return "success"
    return render_template('/admin/admin_login.html')

# 用户注册
@app.route('/user/user_register.html', methods=['GET', 'POST'])
def user_register(name=None):
    if request.method == 'POST':
        print(request.headers)
        print(request.get_json())
        return "success"
    return render_template('/user/user_register.html')

@app.route('/getMsg', methods=['POST'])
def getMsg(msg=None):
    data = request.get_data()
    if request.method == 'POST':
        handleMsg = APP.views.handleMsg.AIResponse(data)
        return handleMsg


if __name__ == '__main__':
    app.run()
