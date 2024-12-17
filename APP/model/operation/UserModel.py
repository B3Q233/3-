import time

from APP.model.entity.User import User
from APP.logs.logConfig import logging
from APP.model.sqltest import get_session
import re

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
        return user
    except Exception as e:
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
        logging.error(f"在根据用户邮箱查找用户信息时出现错误，邮箱: {username}，错误信息: {e}", exc_info=True)
    finally:
        session.close()

