from APP.model.operation.AdminModel import *


def admin_login_check(admin):
    get_admin = find_admin_by_name(admin.admin_name)
    if get_admin is None:
        return '登陆失败，管理员不存在', False
    if get_admin.password != admin.password:
        return '登陆失败，密码错误', False
    return '登陆成功', True


if __name__ == '__main__':
    insert_admin(Admin(admin_name='bbq', password='dnddm543',email='33324@qq.com'))
