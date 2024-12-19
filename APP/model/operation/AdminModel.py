import time
from APP.model.entity.Admin import Admin
from APP.logs.logConfig import logging
from APP.model.sqltest import get_session

# 配置日志记录器
current_time = time.strftime('%Y-%m-%d', time.localtime())
logging.basicConfig(
    level=logging.ERROR,  # 设置日志级别为ERROR，只记录错误信息
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a'  # 追加模式，每次记录日志在文件末尾添加
)


def find_admin_by_id(admin_id):
    """
    根据管理员id查找管理员信息
    """
    session = get_session()
    try:
        admin = session.query(Admin).filter(Admin.admin_id == admin_id).first()
        return admin
    except Exception as e:
        logging.error(f"在根据管理员id查找管理员信息时出现错误，管理员id: {admin_id}，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def find_admin_by_email(email):
    """
    根据管理员邮箱查找管理员信息
    """
    session = get_session()
    try:
        admin = session.query(Admin).filter(Admin.email == email).first()
        return admin
    except Exception as e:
        logging.error(f"在根据管理员邮箱查找管理员信息时出现错误，邮箱: {email}，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def insert_admin(new_admin):
    """
    插入新管理员信息到数据库
    """
    session = get_session()
    try:
        session.add(new_admin)
        session.commit()
    except Exception as e:
        logging.error(f"在插入新管理员信息时出现错误，管理员信息: {new_admin}，错误信息: {e}", exc_info=True)
        session.rollback()
        raise
    finally:
        session.close()


def delete_admin_by_id(admin_id):
    """
    根据管理员id删除管理员信息
    """
    session = get_session()
    try:
        admin = session.query(Admin).filter(Admin.admin_id == admin_id).first()
        if admin:
            session.delete(admin)
            session.commit()
        return admin
    except Exception as e:
        logging.error(f"在根据管理员id删除管理员信息时出现错误，管理员id: {admin_id}，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def update_admin_info(admin_id, updated_admin_data):
    """
    根据管理员id更新管理员信息
    """
    session = get_session()
    try:
        admin = session.query(Admin).filter(Admin.admin_id == admin_id).first()
        if admin:
            # 假设updated_admin_data是一个字典，包含要更新的字段和对应的值
            for key, value in updated_admin_data.items():
                setattr(admin, key, value)
            session.commit()
        return admin
    except Exception as e:
        logging.error(f"在根据管理员id更新管理员信息时出现错误，管理员id: {admin_id}，错误信息: {e}", exc_info=True)
    finally:
        session.close()
