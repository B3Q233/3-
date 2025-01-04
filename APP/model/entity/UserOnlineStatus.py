from sqlalchemy import Column, Integer, Boolean, DateTime
from sqlalchemy.orm import declarative_base

from APP.model import db_pool

Base = declarative_base()

class UserOnlineStatus(Base):
    """
    UserOnlineStatus类用于表示系统中的用户在线状态和上次签到时间信息，对应数据库中的用户在线状态表。

    定义了用户在线状态相关的属性以及与数据库表结构的映射关系，方便进行数据库操作。
    """
    __tablename__ = 'user_online_status'

    # 定义用户在线状态id字段，为主键且自动递增
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 定义关联的用户id字段，并设置为外键
    user_id = Column(Integer, nullable=False,unique=True)
    # 定义用户是否在线字段
    is_online = Column(Boolean, default=False, nullable=False)
    # 定义用户上次签到时间字段
    last_sign_in_time = Column(DateTime, default=None)


    def __init__(self, user_id=None, is_online=False, last_sign_in_time=None):
        """
        初始化UserOnlineStatus类实例。
        参数:
        - user_id: 关联用户的唯一标识符，整数类型
        - is_online: 用户是否在线，布尔类型
        - last_sign_in_time: 用户上次签到时间，DateTime类型
        """
        self.user_id = user_id
        self.is_online = is_online
        self.last_sign_in_time = last_sign_in_time

    def to_dict(self):
        """
        将UserOnlineStatus实例转换为字典。
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'is_online': self.is_online,
            'last_sign_in_time': self.last_sign_in_time,
        }

if __name__ == '__main__':
    Base.metadata.create_all(db_pool.engine)