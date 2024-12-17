from APP.model.operation.UserModel import *


def user_register_check(new_user):
    if find_user_by_username(new_user.username) is not None:
        return '注册失败,用户名已经存在',False
    if find_user_by_email(new_user.email) is not None:
        return '注册失败,邮箱已经注册',False
    new_user.api_key = 'e7d7fe0a829e0872b438334405c37a8c.xRof5ICQsaRtFf6u'
    new_user.quota = 100
    insert_user(new_user)
    return '注册成功',True


def user_login_check(new_user):
    get_user = find_user_by_username(new_user.username)
    if get_user is None:
        return '登陆失败，用户名不存在',False
    if get_user.password != new_user.password:
        return '登陆失败，密码错误',False
    return '登陆成功',True
