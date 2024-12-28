import json

from APP.model.entity.Admin import *
from APP.model.entity.User import *
from APP.model.service import UserService, AdminService, ModelService
from APP.utils.tool import *
from APP.model.entity.Model import *


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
    msg, status = AdminService.admin_login_check(admin)
    if status is False:
        user, ret_status = UserService.get_user_by_username(admin_name)
        if ret_status:
            if user.level > 0:
                status = True
                msg = '登录成功'
    if status:
        status = 1
    else:
        status = 0
    ret_msg = {'msg': msg, 'status': status}
    return json.dumps(ret_msg)


# 获取全部用户
def get_users():
    return json.dumps({'status': 1, 'data': UserService.get_all_users()})


# 获取全部AI模型
def get_AI():
    return json.dumps({'status': 1, 'data': ModelService.get_all_AI()})


# 用户权限提升
def user_level_up(request):
    decoded_data = request.data.decode('utf-8')
    # 解析查询字符串
    parsed_data = parse_qs(decoded_data)
    # 获取属性值
    user_id = parsed_data.get('user_id')[0]
    ret_msg, status = UserService.update_user_level(user_id, 1)
    if status:
        status = 1
    else:
        status = 0
    return json.dumps({'status': status, 'msg': ret_msg})


# 用户删除
def user_delete(request):
    decoded_data = request.data.decode('utf-8')
    # 解析查询字符串
    parsed_data = parse_qs(decoded_data)
    # 获取属性值
    user_id = parsed_data.get('user_id')[0]
    ret_msg, status = UserService.delete_user_by_id(user_id)
    if status:
        status = 1
    else:
        status = 0
    return json.dumps({'status': status, 'msg': ret_msg})


# 用户修改
def user_modify(request):
    get_data = parse_data(request)
    user_id = get_data.get('user_id')[0]
    username = get_data['username'][0]
    email = unquote(get_data['email'][0])
    password = get_data['password'][0]
    new_user = User(id=user_id, username=username, password=password, email=email)
    ret_msg, status = UserService.update_whole_user(new_user)
    return json.dumps({'status': status, 'msg': ret_msg})


# 模型添加
def model_add(request):
    get_data = parse_data(request)
    model_name = get_data.get('model_name')
    model_category = get_data['model_category'][0]
    initial_text = unquote(get_data['initial_text'][0])
    model_description = unquote(get_data['model_description'][0])
    new_model = Model(model_name=model_name, model_category=model_category, initial_text=initial_text, model_description=model_description)
    msg,status = ModelService.model_add(new_model)
    return json.dumps({'status': status, 'msg': msg})


if __name__ == '__main__':
    print(user_level_up('1'))
