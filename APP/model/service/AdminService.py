from APP.model.DAO import AdminDAO
from APP.model.DAO.AdminDAO import *


def get_admin_by_name(admin_name):
    return AdminDAO.find_admin_by_name(admin_name)


def admin_login_check(admin):
    get_admin = find_admin_by_name(admin.admin_name)
    if get_admin is None:
        return '登陆失败，管理员不存在', False
    if get_admin.password != admin.password:
        return '登陆失败，密码错误', False
    return '登陆成功', True


def user_level_up(get_user):
    get_admin = get_admin_by_name(get_user.username)
    if get_admin is not None:
        return '该用户已经是管理员了，请不要重复升级', False
    insert_admin(Admin(admin_name=get_user.username, password=get_user.password, email=get_user.email))
    return '升级成功', True


def user_delete(user_id):
    pass


if __name__ == '__main__':
    insert_admin(Admin(admin_name='bbq', password='dnddm543', email='33324@qq.com'))
