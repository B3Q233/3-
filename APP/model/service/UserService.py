from APP.model.operation import UserModel

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
    return '登陆成功', True


# 获取全部用户

def get_all_users():
    user_list = []
    users = find_all_users()
    for user in users:
        user_dict = user.to_dict()
        user_list.append(user_dict)
    return user_list


def get_user_by_id(user_id):
    user = find_user_by_id(user_id)
    if user is None:
        return '该用户不存在', False
    return user, True


def get_user_by_username(username):
    user = find_user_by_username(username)
    if user is None:
        return '该用户不存在', False
    return user, True


def delete_user_by_id(user_id):
    user = find_user_by_id(user_id)
    if user is None:
        return '删除失败，该用户不存在', False
    status = UserModel.delete_user_by_id(user_id)
    if status:
        return '删除成功', True
    return '删除失败，请检查网络', False


def update_whole_user(new_user):
    status = UserModel.update_whole_user(new_user)
    if status:
        return '更新用户成功', True
    return '更新用户失败', False


def update_user_quota(user_id, new_quota):
    status = UserModel.update_user_quota(user_id, new_quota)
    return status


def update_user_level(user_id, new_level):
    status = UserModel.update_user_level(user_id, new_level)
    if status:
        return '更新用户权限成功', True
    return '更新用户权限失败', False


if __name__ == '__main__':
    print(get_user_by_username('admin1'))
