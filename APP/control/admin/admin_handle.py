import json

from APP.model.service.AdminService import *
from APP.model.service.UserService import *
from APP.model.service.ModelService import *


# 管理员登录判断
def login_check(request):
    decoded_data = request.data.decode('utf-8')
    # 解析查询字符串
    parsed_data = parse_qs(decoded_data)
    # 获取属性值
    admin_name = parsed_data.get('username')[0]
    admin_pwd = parsed_data.get('password')[0]
    if admin_name is None:
        admin_name = ''
    if admin_pwd is None:
        admin_pwd = ''
    admin = Admin(admin_name=admin_name, password=admin_pwd)
    msg, status = admin_login_check(admin)
    if status:
        status = 1
    else:
        status = 0
    ret_msg = {'msg': msg, 'status': status}
    return json.dumps(ret_msg)


# 获取全部用户
def get_users():
    return json.dumps({'status': 1, 'data': get_all_users()})


# 获取全部AI模型
def get_AI():
    return json.dumps({'status': 1, 'data': get_all_AI()})


