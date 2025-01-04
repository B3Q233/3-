from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# 假设sqltest模块已经定义了engine
from APP.model import db_pool

Base = declarative_base()


class Admin(Base):
    """
    Admin类用于表示系统中的管理员信息，对应数据库中的管理员表。

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

    def __init__(self, admin_id=None, admin_name=None, password=None, email=None):
        """
        初始化Admin类实例。
        参数:
        - admin_id: 管理员的唯一标识符，整数类型，默认值为None，数据库操作时可自动递增生成。
        - admin_name: 管理员的姓名，字符串类型
        - password: 管理员的密码，字符串类型
        - email: 管理员的邮箱地址，字符串类型
        """
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.password = password
        self.email = email

    def to_dict(self):
        """
        将Admin实例转换为字典。
        """
        return {
            'admin_id': self.admin_id,
            'admin_name': self.admin_name,
            'password': self.password,
            'email': self.email
        }


if __name__ == '__main__':
    # 创建数据库表
    Base.metadata.create_all(sqltest.engine)

    # 创建一个Admin实例并转换为字典
    admin_instance = Admin(admin_name='John Doe', password='password123', email='john@example.com')
    admin_dict = admin_instance.to_dict()
    print(admin_dict)
