import json
from flask import session

from APP.model.operation.UserModel import *
from APP.utils.tool import *


# 用户注册
def user_register_check(new_user):
    if not (validate_name(new_user.username) and validate_email(new_user.email) and validate_password(
            new_user.password)):
        return '格式错误', False
    if find_user_by_username(new_user.username) is not None:
        return '注册失败,用户名已经存在', False
    if find_user_by_email(new_user.email) is not None:
        return '注册失败,邮箱已经注册', False
    new_user.api_key = 'e7d7fe0a829e0872b438334405c37a8c.xRof5ICQsaRtFf6u'
    new_user.quota = 100
    insert_user(new_user)
    return '注册成功', True


# 用户登录
def user_login_check(new_user):
    get_user = find_user_by_username(new_user.username)
    if get_user is None:
        return '登陆失败，用户名不存在', False
    if get_user.password != new_user.password:
        return '登陆失败，密码错误', False
    print(session.get('user_id'))
    if session.get('user_id') is None:
        session['user_id'] = get_user.id
        return '登陆成功', True
    return '该账号已经登录，请先注销',False




# 获取全部用户

def get_all_users():
    user_list = []
    users = find_all_users()
    for user in users:
        user_list.append(user.to_dict())
    return user_list


if __name__ == '__main__':
    print(get_all_users())
