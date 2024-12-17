from sqlalchemy import create_engine, Column, Integer, String, Index
from sqlalchemy.orm import declarative_base
from APP.model import sqltest

Base = declarative_base()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:password@localhost/dbname?charset=utf8", echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'  # 数据库表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(30), nullable=False, unique=True)
    api_key = Column(String(255), nullable=False)
    password = Column(String(20), nullable=False)
    username = Column(String(20), nullable=False, unique=True)
    quota = Column(Integer)

    __table_args__ = (
        Index('ix_unique_users_id', id, unique=True),
    )

    __mapper_args__ = {
        'primary_key': [id],
    }

    def __init__(self, id=None, email=None, api_key=None, password=None, username=None,quota=None):
        self.id = id
        self.email = email
        self.api_key = api_key
        self.password = password
        self.username = username
        self.quota = quota


if __name__ == '__main__':
    u = User()
    Base.metadata.create_all(sqltest.engine)
    pass
