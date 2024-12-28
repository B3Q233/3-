import time

from APP.model.entity.User import User
from APP.logs.logConfig import logging
from APP.model.sqltest import get_session

# 配置日志记录器
current_time = time.strftime('%Y-%m-%d', time.localtime())
logging.basicConfig(
    level=logging.ERROR,  # 设置日志级别为ERROR，只记录错误信息
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a'  # 追加模式，每次记录日志在文件末尾添加
)


def find_user_by_id(user_id):
    """
    根据用户id查找用户信息
    """
    session = get_session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        return user
    except Exception as e:
        session.rollback()
        logging.error(f"在根据用户id查找用户信息时出现错误，用户id: {user_id}，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def find_user_by_email(email):
    """
    根据用户邮箱查找用户信息
    """
    session = get_session()
    try:
        user = session.query(User).filter(User.email == email).first()
        return user
    except Exception as e:
        session.rollback()
        logging.error(f"在根据用户邮箱查找用户信息时出现错误，邮箱: {email}，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def insert_user(new_user):
    """
    插入新用户信息到数据库
    """
    session = get_session()
    try:
        session.add(new_user)
        session.commit()
    except Exception as e:
        logging.error(f"在插入新用户信息时出现错误，用户信息: {new_user}，错误信息: {e}", exc_info=True)
        session.rollback()
        raise
    finally:
        session.close()


def delete_user_by_id(user_id):
    """
    根据用户id删除用户信息
    """
    session = get_session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        logging.error(f"在根据用户id删除用户信息时出现错误，用户id: {user_id}，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def find_user_by_username(username):
    """
        根据用户名查找用户
    """
    session = get_session()
    try:
        user = session.query(User).filter(User.username == username).first()
        return user
    except Exception as e:
        session.rollback()
        logging.error(f"在根据用户邮箱查找用户信息时出现错误，邮箱: {username}，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def find_all_users():
    """
        查找所有用户
    """
    session = get_session()
    try:
        users = session.query(User).all()
        return users
    except Exception as e:
        session.rollback()
        logging.error(f"在查找所有用户信息时出现错误，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def update_whole_user(to_update_user):
    """
            更新用户的所有信息
    """
    session = get_session()
    try:
        user = session.query(User).filter(User.id == to_update_user.id).first()
        if user:
            user.username = to_update_user.username
            user.email = to_update_user.email
            user.password = to_update_user.password
            user.quota = to_update_user.quota
            user.level = to_update_user.level
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        logging.error(f"在更新用户的所有信息时出现错误，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def update_user_level(user_id, new_level):
    """
            更新用户的级别
    """
    session = get_session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.level = new_level
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        logging.error(f"在更新用户的级别时出现错误，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def update_user_quota(user_id, delta_quota):
    """
            更新用户的额度
    """
    session = get_session()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.quota += delta_quota
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        logging.error(f"在更新用户的额度时出现错误，错误信息: {e}", exc_info=True)
    finally:
        session.close()


if __name__ == '__main__':
    # insert_user(User(username='admin1', email='<EMAIL>', password='<PASSWORD>'))
    # update_whole_user(User(id=1, username='admin123', email='<EMAIL>', password='<PASSWORD>'))
    pass