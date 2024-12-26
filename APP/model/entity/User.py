from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.orm import declarative_base

from APP.model import sqltest

Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(30), nullable=False, unique=True)
    api_key = Column(String(255), nullable=False)
    password = Column(String(20), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    quota = Column(Integer)


    __mapper_args__ = {
        'primary_key': [id],
    }

    def __init__(self, email=None, api_key=None, password=None, username=None, quota=None):
        self.email = email
        self.api_key = api_key
        self.password = password
        self.username = username
        self.quota = quota

    def to_dict(self):
        """
        将User实例转换为字典。

        返回:
        - 一个包含用户属性的字典。
        """
        return {
            'id': self.id,
            'email': self.email,
            'api_key': self.api_key,
            'password': self.password,
            'username': self.username,
            'quota': self.quota
        }

if __name__ == '__main__':
    # 创建数据库表
    Base.metadata.create_all(sqltest.engine)

    # 创建User实例并转换为字典
    user_instance = User(email='example@example.com', api_key='api_key_here', password='password123', username='username', quota=1000)
    user_dict = user_instance.to_dict()
    print(user_dict)
