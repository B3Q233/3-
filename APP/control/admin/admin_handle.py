import json

from APP.model.entity.Admin import *
from APP.model.entity.User import *
from APP.model.service import UserService, AdminService, ModelService
from APP.utils.tool import *
from APP.model.entity.Model import *
from APP.app import set_session_id_to_user
from APP.app import get_session_id_to_user
from APP.app import set_session_id_to_user, get_session_id_to_user, delete_session_id_to_user


# 管理员登录判断
def login_check(request,online_users):
    decoded_data = request.data.decode('utf-8')
    # 解析查询字符串
    parsed_data = parse_qs(decoded_data)
    session_id = request.cookies.get('session')
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
                ret_status = 1 if ret_status else 0
                real_admin,user_status = UserService.get_user_by_username(admin_name)
                ret_msg = {'status': ret_status, 'data': {'admin_name': real_admin.username,'admin_id':real_admin.id,'email':real_admin.email,'admin_password':'************************'}}
                return json.dumps(ret_msg)
            ret_msg = {'status': ret_status, 'data': "管理员不存在"}
            return json.dumps(ret_msg)
    if status:
        set_session_id_to_user(session_id, 1,online_users)
        real_admin = AdminService.get_admin_by_name(admin_name).to_dict()
        real_admin['admin_password'] = '***********************'
        status = 1
        ret_msg = {'status': status, 'data': real_admin}
    else:
        status = 0
        ret_msg = {'status': status, 'data': msg}

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


def get_user_by_username(request):
    get_data = parse_data(request)
    username = get_data['username'][0]
    ret_msg, status = UserService.get_user_by_username(username)
    ret_msg = ret_msg.to_dict()
    ret_msg['password'] = '************'
    if status:
        status = 1
        ret_msg = {'status': status, 'data': ret_msg}
        return json.dumps(ret_msg)
    ret_msg = {'status': 0, 'data': None}
    return json.dumps(ret_msg)

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
    model_name = get_data.get('model_name')[0]
    model_id = get_data.get('model_id')
    if model_id is not None:
        model_id = model_id[0]
    model_category = get_data['model_category'][0]
    initial_text = get_data['initial_text'][0]
    model_description = get_data['model_description'][0]
    if model_id is not None:
        new_model = Model(model_id=model_id, model_name=model_name, model_category=model_category,
                          initial_text=initial_text,
                          model_description=model_description)
        msg, status = ModelService.whole_model_update(new_model)
    else:
        new_model = Model(model_name=model_name, model_category=model_category,
                          initial_text=initial_text,
                          model_description=model_description)
        msg, status = ModelService.model_add(new_model)
    if status:
        status = 1
    else:
        status = 2
    return json.dumps({'status': status, 'msg': msg})


# 根据模型id获取模型
def get_model_by_id(request):
    get_data = parse_data(request)
    model_id = get_data.get('model_id')[0]
    data, status = ModelService.get_model_by_id(model_id)
    if status:
        status = 1
    else:
        status = 2
    return json.dumps({'status': status, 'data': data})


# 根据id删除模型
def model_delete(request):
    get_data = parse_data(request)
    model_id = get_data.get('model_id')[0]
    msg, status = ModelService.model_delete(model_id)
    if status:
        status = 1
    else:
        status = 2
    return json.dumps({'msg': msg, 'status': status})


if __name__ == '__main__':
    print(user_level_up('1'))
