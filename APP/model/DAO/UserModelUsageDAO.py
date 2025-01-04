import time
from datetime import datetime

from APP.logs.logConfig import logging
from APP.model.db_pool import get_session
from APP.model.entity.UserModelUsage import *

# 配置日志记录器
current_time = time.strftime('%Y-%m-%d', time.localtime())
logging.basicConfig(
    level=logging.ERROR,  # 设置日志级别为ERROR，只记录错误信息
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a'  # 追加模式，每次记录日志在文件末尾添加
)


def find_usage_by_id(user_id, model_id):
    """
    根据用户id和模型id查找使用记录
    """
    session = get_session()
    try:
        usage = session.query(UserModelUsage).filter(
            UserModelUsage.user_id == user_id,
            UserModelUsage.model_id == model_id
        ).first()
        return usage
    except Exception as e:
        logging.error(f"在根据用户id和模型id查找使用记录时出现错误，用户id: {user_id}，模型id: {model_id}，错误信息: {e}",
                      exc_info=True)
    finally:
        session.close()


def insert_usage(new_usage):
    """
    插入新的使用记录到数据库
    """
    session = get_session()
    try:
        session.add(new_usage)
        session.commit()
    except Exception as e:
        logging.error(f"在插入新的使用记录时出现错误，使用记录信息: {new_usage}，错误信息: {e}", exc_info=True)
        session.rollback()
        raise
    finally:
        session.close()


def delete_usage_by_id(user_id, model_id):
    """
    根据用户id和模型id删除使用记录
    """
    session = get_session()
    try:
        usage = session.query(UserModelUsage).filter(
            UserModelUsage.user_id == user_id,
            UserModelUsage.model_id == model_id
        ).first()
        if usage:
            session.delete(usage)
            session.commit()
        return usage
    except Exception as e:
        logging.error(f"在根据用户id和模型id删除使用记录时出现错误，用户id: {user_id}，模型id: {model_id}，错误信息: {e}",
                      exc_info=True)
    finally:
        session.close()


def update_usage_content(user_model_usage):
    """
        根据用户id和模型id更新使用记录信息
        """
    session = get_session()
    try:
        usage = session.query(UserModelUsage).filter(
            UserModelUsage.user_id == user_model_usage.user_id,
            UserModelUsage.model_id == user_model_usage.model_id
        ).first()
        if usage:
            usage.usage_time = datetime.now()
            usage.usage_content = user_model_usage.usage_content
            session.commit()
            return True
        return False
    except Exception as e:
        logging.error(
            f"在根据用户id和模型id更新使用记录信息时出现错误，用户id: {UserModelUsage.user_id}，模型id: {UserModelUsage.model_id}，错误信息: {e}",
            exc_info=True)
    finally:
        session.close()


if __name__ == '__main__':
    usage_time_str = datetime.today().strftime('%Y-%m-%d %H:%M')
    # 使用正确的格式字符串来解析日期和时间
    usage_time = datetime.strptime(usage_time_str, '%Y-%m-%d %H:%M')

    # 创建UserModelUsage实例时，确保usage_time是datetime对象
    new_usage = update_usage_content(UserModelUsage(
        user_id=4,
        model_id=8,
        usage_content="1231"
    ))
