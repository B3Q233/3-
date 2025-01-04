import json
from datetime import time, datetime

from flask import session

import APP.app
from APP.model.entity.User import *
from APP.model.entity.UserOnlineStatus import *
from APP.model.service import UserService
from APP.model.service import UserOnlineStatusService
from urllib.parse import unquote, parse_qs
from APP.utils.tool import parse_data



def get_user_login_status(user_id):
    _,status = UserOnlineStatusService.get_user_online_status(user_id)
    return status


def is_login(get_user_name):
    get_user, ret_msg = UserService.get_user_by_username(get_user_name)
    print(ret_msg)
    if ret_msg and get_user_login_status(get_user.id):
        return '该账户已经在其它地方登录,请登出后重试', False
    return 'ok', True


# 用户登录
def login_check(request,online_users):
    decoded_data = request.data.decode('utf-8')
    session_id = request.cookies.get('session')
    # 解析查询字符串
    parsed_data = parse_qs(decoded_data)
    # 获取属性值
    username = parsed_data.get('username')[0]
    password = parsed_data.get('password')[0]
    msg, status = is_login(username)
    if not status:
        ret_msg = {'status': status, 'data': msg}
        return json.dumps(ret_msg)
    else:
        new_user = User(username=username, password=password)
        msg, status = UserService.user_login_check(new_user)
        get_user, ret_msg = UserService.get_user_by_username(username)
        if status:
            status = 1
            ret_user = get_user.to_dict()
            ret_user['password'] = '******************'
            ret_msg = {'status': status, 'data': ret_user}
            APP.app.set_session_id_to_user(session_id,0,online_users)
            _,ret_status = UserOnlineStatusService.change_user_online_status(get_user.id,True)
            if not ret_status:
                date_string = "1970-01-01"
                date_format = "%Y-%m-%d"
                date_datetime = datetime.strptime(date_string, date_format)
                UserOnlineStatusService.inset_new_user_online_status(UserOnlineStatus(user_id=get_user.id,is_online=True,last_sign_in_time=date_datetime))
        else:
            status = 0
            ret_msg = {'status': status, 'data': get_user}

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
    msg, status = UserService.user_register_check(new_user)
    if status:
        status = 1
    else:
        status = 0
    ret_msg = {'msg': msg, 'status': status}
    return json.dumps(ret_msg)


# 获取单个用户信息
def get_user_info(request):
    get_data = parse_data(request)
    user_id = get_data.get('user_id')
    user, status = UserService.get_user_by_id(user_id)
    user = user.to_dict()
    user['password'] = "**************"
    if status:
        status = 1
        ret_msg = {'data': user.to_dict(), 'status': status}
    else:
        status = 0
        ret_msg = {'data': user.to_dict(), 'status': status}
    return json.dumps(ret_msg)

def user_sign_in(request):
    get_data = parse_data(request)
    user_id = get_data.get('user_id')
    msg,status = UserOnlineStatusService.update_user_sign_time(user_id)
    if status:
        status = 1
        UserService.update_user_quota(user_id, 20)
    else:
        status = 0
    ret_msg = {'msg': msg, 'status': status}
    return json.dumps(ret_msg)

def user_sign_out(request):
    get_data = parse_data(request)
    user_id = get_data.get('user_id')
    msg,status = UserOnlineStatusService.change_user_online_status(user_id, False)
    return msg,status

if __name__ == '__main__':
    origin_data = {
        'data': b'{user_id:1}'
    }
    print(get_user_info(request=origin_data))
