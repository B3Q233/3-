from datetime import datetime, timedelta
from APP.model.DAO import UserOnlineStatusDAO


def get_user_online_status(user_id):
    try:
        # 尝试获取用户的在线状态
        status = UserOnlineStatusDAO.find_user_online_status(user_id)
        if status is None:
            # 如果状态为None，则用户不存在
            return None, False
        else:
            # 否则返回成功消息和状态
            return '成功获取', status
    except Exception as e:
        # 如果发生异常，返回错误消息和异常信息
        return f'获取用户在线状态时发生错误: {e}', None


def change_user_online_status(user_id, status):
    try:
        # 首先检查用户是否存在
        msg, ret_status = get_user_online_status(user_id)
        if msg is not None:
            # 如果用户存在，尝试更新在线状态
            success = UserOnlineStatusDAO.update_user_online_status(user_id, status)
            if success:
                # 如果更新成功，返回成功消息
                return '更新成功', True
            else:
                # 如果更新失败，返回失败消息
                return '更新失败', False
        else:
            # 如果用户不存在，返回用户不存在消息
            return '用户不存在', False
    except Exception as e:
        # 如果发生异常，返回错误消息和异常信息
        return f'更新用户在线状态时发生错误: {e}', False


def update_user_sign_time(user_id):
    try:
        # 尝试获取用户的最后签到时间
        last_sign_in_time = UserOnlineStatusDAO.find_last_sign_in_time_by_id(user_id)
        if last_sign_in_time is None:
            # 如果时间为None，则用户不存在
            return '用户不存在', False

        # 格式化最后签到时间和当前时间
        last_sign_in_time = last_sign_in_time.strftime('%Y-%m-%d')
        now_time = datetime.now().strftime('%Y-%m-%d')
        last_sign_in_date = datetime.strptime(last_sign_in_time, '%Y-%m-%d')
        now_date = datetime.strptime(now_time, '%Y-%m-%d')

        # 计算时间差
        delta = now_date - last_sign_in_date

        # 如果时间差大于等于1天，则更新签到时间
        if delta >= timedelta(days=1):
            success = UserOnlineStatusDAO.update_user_last_sign_in_time(user_id)
            return '签到成功', success
        else:
            # 如果时间差小于1天，则用户今天已经签到
            return '您今天已经签到，请明天再签到', False
    except Exception as e:
        # 如果发生异常，返回错误消息和异常信息
        return f'更新用户签到时间时发生错误: {e}', False

def inset_new_user_online_status(new_status):
    UserOnlineStatusDAO.insert_new_status(new_status)

if __name__ == '__main__':
    print(get_user_online_status(1))
