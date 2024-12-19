from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from APP.model import sqltest

Base = declarative_base()


class Model(Base):
    """
    BigModel类用于表示系统中的大模型信息，对应数据库中的大模型表。

    定义了大模型相关的属性以及与数据库表结构的映射关系，方便进行数据库操作。
    """
    __tablename__ = 'models'

    # 定义模型id字段，为主键且自动递增
    model_id = Column(Integer, primary_key=True, autoincrement=True)
    # 定义模型名字段
    model_name = Column(String(100), nullable=False)
    # 定义模型类别字段
    model_category = Column(String(50), nullable=False)
    # 定义初始文本字段
    initial_text = Column(String(500), nullable=False)

    def __init__(self, model_id=None, model_name=None, model_category=None, initial_text=None):
        """
        初始化BigModel类实例。

        参数:
        - model_id: 大模型的唯一标识符，整数类型，默认值为None，数据库操作时可自动递增生成。
        - model_name: 大模型的名称，字符串类型，最大长度100，不能为空，默认值为None。
        - model_category: 大模型的类别，字符串类型，最大长度50，不能为空，默认值为None。
        - initial_text: 大模型的初始文本，字符串类型，最大长度500，不能为空，默认值为None。
        """
        self.model_id = model_id
        self.model_name = model_name
        self.model_category = model_category
        self.initial_text = initial_text


if __name__ == '__main__':
    u = Model()
    Base.metadata.create_all(sqltest.engine)
    pass
