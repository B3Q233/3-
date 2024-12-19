from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from APP.model import sqltest

Base = declarative_base()


class Admin(Base):
    """
    Administrator类用于表示系统中的管理员信息，对应数据库中的管理员表。

    定义了管理员相关的属性以及与数据库表结构的映射关系，方便进行数据库操作。
    """
    __tablename__ = 'admin'

    # 定义管理员id字段，为主键且自动递增
    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    # 定义管理员名字段
    admin_name = Column(String(50), nullable=False)
    # 定义密码字段
    password = Column(String(20), nullable=False)
    # 定义邮箱字段
    email = Column(String(20), nullable=False)

    def __init__(self, administrator_id=None, administrator_name=None, password=None, email=None):
        """
        初始化Administrator类实例。
        参数:
        - administrator_id: 管理员的唯一标识符，整数类型，默认值为None，数据库操作时可自动递增生成。
        - administrator_name: 管理员的姓名，字符串类型
        - password: 管理员的密码，字符串类型
        - email: 管理员的邮箱地址，字符串类型
        """
        self.administrator_id = administrator_id
        self.administrator_name = administrator_name
        self.password = password
        self.email = email


if __name__ == '__main__':
    u = Admin()
    Base.metadata.create_all(sqltest.engine)
    pass