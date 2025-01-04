from APP.model.DAO import UserModelUsageDAO
from APP.model.entity.UserModelUsage import *


# 根据用户id 和 模型id 查找信息
def get_usage_history(user_id, model_id):
    ret_usage = UserModelUsageDAO.find_usage_by_id(user_id, model_id)
    return ret_usage.to_dict()


# 插入使用记录
def insert_usage(new_usage):
    get_usage = UserModelUsageDAO.find_usage_by_id(new_usage.user_id, new_usage.model_id)
    if get_usage:
        return update_usage(new_usage)
    UserModelUsageDAO.insert_usage(new_usage)


# 更新
def update_usage(new_usage):
    return UserModelUsageDAO.update_usage_content(new_usage)


if __name__ == '__main__':
    insert_usage(UserModelUsage(user_id=4, model_id=8,usage_content='123'))
