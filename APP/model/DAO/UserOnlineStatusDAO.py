import time
from datetime import datetime

from APP.logs.logConfig import logging
from APP.model.db_pool import get_session
from APP.model.entity.UserOnlineStatus import UserOnlineStatus

# 配置日志记录器
# current_time = time.strftime('%Y-%m-%d', time.localtime())
# logging.basicConfig(
#     level=logging.ERROR,  # 设置日志级别为ERROR，只记录错误信息
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     filename=f'logs/{current_time}.log',  # 设置日志文件名
#     filemode='a'  # 追加模式，每次记录日志在文件末尾添加
# )

def insert_new_status(new_status):
    """
    插入新的用户在线状态记录到数据库
    """
    session = get_session()
    try:
        # 创建一个新的 UserOnlineStatus 实例
        user_status = UserOnlineStatus(
            user_id=new_status.user_id,
            is_online=new_status.is_online,
            last_sign_in_time=new_status.last_sign_in_time,
        )
        session.add(user_status)
        session.commit()
        return True
    except Exception as e:
        # 如果发生错误，回滚会话
        session.rollback()
        print(f"在插入新的用户在线状态时出现错误，状态信息: {new_status}，错误信息: {e}")
        return False
    finally:
        # 关闭会话
        session.close()

def find_last_sign_in_time_by_id(user_id):
    """
    根据用户id查找最后一次签到时间
    """
    session = get_session()
    try:
        user_status = session.query(UserOnlineStatus).filter(
            UserOnlineStatus.user_id == user_id
        ).first()
        return user_status.last_sign_in_time if user_status else None
    except Exception as e:
        logging.error(f"在根据用户id查找签到记录时出现错误，用户id: {user_id}，错误信息: {e}",
                      exc_info=True)
    finally:
        session.close()

def find_user_online_status(user_id):
    """
    根据用户id查找最后一次签到时间
    """
    session = get_session()
    try:
        user_status = session.query(UserOnlineStatus).filter(
            UserOnlineStatus.user_id == user_id
        ).first()
        return user_status.is_online if user_status else None
    except Exception as e:
        logging.error(f"在根据用户id查找签到记录时出现错误，用户id: {user_id}，错误信息: {e}",
                      exc_info=True)
    finally:
        session.close()

def update_user_online_status(user_id, status):
    """
    根据用户id更新在线状态
    """
    session = get_session()
    try:
        user_status = session.query(UserOnlineStatus).filter(
            UserOnlineStatus.user_id == user_id
        ).first()
        if user_status:
            user_status.is_online = status
            session.commit()
            return True
        return False
    except Exception as e:
        logging.error(
            f"在根据用户id更新在线状态信息时出现错误，用户id: {user_id}，错误信息: {e}",
            exc_info=True)
    finally:
        session.close()

def update_user_last_sign_in_time(user_id):
    """
    根据用户id更新最后一次签到时间
    """
    session = get_session()
    try:
        user_status = session.query(UserOnlineStatus).filter(
            UserOnlineStatus.user_id == user_id
        ).first()
        if user_status:
            user_status.last_sign_in_time = datetime.now()
            session.commit()
            return True
        return False
    except Exception as e:
        logging.error(
            f"在根据用户id更新最后一次签到时间时出现错误，用户id: {user_id}，错误信息: {e}",
            exc_info=True)
    finally:
        session.close()

if __name__ == '__main__':
    new_status = UserOnlineStatus(
        user_id=1,  # 假设的用户ID
        is_online=True,  # 用户在线状态
        last_sign_in_time=datetime.now()  # 可选，如果提供则使用该时间，否则使用当前时间
    )
