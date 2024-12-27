import json
from flask import session
from APP.model.entity.User import *
from APP.model.service import UserService
from APP.model.service.UserService import *
from urllib.parse import unquote, parse_qs


# 用户登录
def login_check(request):
    decoded_data = request.data.decode('utf-8')
    # 解析查询字符串
    parsed_data = parse_qs(decoded_data)
    # 获取属性值
    username = parsed_data.get('username')[0]
    password = parsed_data.get('password')[0]
    new_user = User(username=username, password=password)
    msg, status = UserService.user_login_check(new_user)
    if status:
        status = 1
    else:
        status = 0
    ret_msg = {'msg': msg, 'status': status}
    return json.dumps(ret_msg)


# 用户注册
def register_check(request):
    decoded_data = request.data.decode('utf-8')
    # 解析查询字符串
    parsed_data = parse_qs(decoded_data)
    # 获取属性值
    username = parsed_data['username'][0]
    email = unquote(parsed_data['email'][0])
    password = parsed_data['password'][0]
    new_user = User(username=username, password=password, email=email)
    msg, status = user_register_check(new_user)
    if status:
        status = 1
    else:
        status = 0
    ret_msg = {'msg': msg, 'status': status}
    return json.dumps(ret_msg)


def get_user_info(request):
    get_data = parse_data(request)
    user_id = get_data.get('user_id')
    data, status = UserService.get_user_by_id(user_id)
    ret_msg = {}
    if status:
        status = 1
        ret_msg = {'data': data, 'status': status}
    else:
        status = 0
        ret_msg = {'data': data, 'status': status}
    print(ret_msg)
    return json.dumps(ret_msg)


if __name__ == '__main__':
    get_user_info(request='user_id=1')
