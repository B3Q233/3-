from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, PrimaryKeyConstraint, Text
from sqlalchemy.orm import declarative_base

from APP.model import db_pool

Base = declarative_base()


class UserModelUsage(Base):
    """
    UserModelUsage类用于表示用户使用大模型的相关信息，对应数据库中的相关表。

    定义了用户使用大模型相关的属性以及与数据库表结构的映射关系，方便进行数据库操作。
    """
    __tablename__ = 'user_model_usage'

    # 定义用户id字段
    user_id = Column(Integer, nullable=False)
    # 定义模型id字段
    model_id = Column(Integer, nullable=False)
    # 定义使用内容字段
    usage_content = Column(Text, nullable=False)
    # 定义使用时间字段，使用DateTime类型来存储时间信息
    usage_time = Column(DateTime)
    PrimaryKeyConstraint(user_id, model_id)

    def __init__(self, user_id=None, model_id=None,usage_content=None, usage_time=None):
        """
        初始化UserModelUsage类实例。
        参数:
        - user_id: 用户的唯一标识符，整数类型
        - model_id: 所使用大模型的唯一标识符，整数类型
        - usage_content: 使用大模型的具体内容，字符串类型
        - usage_time: 使用大模型的时间，DateTime类型
        """
        self.user_id = user_id
        self.model_id = model_id
        self.usage_content = usage_content
        self.usage_time = usage_time

    def to_dict(self):
        """
        将UserModelUsage实例转换为字典。
        """
        return {
            'user_id': self.user_id,
            'model_id': self.model_id,
            'usage_content': self.usage_content,
            'usage_time': self.usage_time
        }


if __name__ == '__main__':
    pass