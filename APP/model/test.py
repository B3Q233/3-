from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:dnddm543@localhost/aichat?charset=utf8",
                       echo=True,
                       pool_size=8,
                       pool_recycle=60*30
                       )


Base = declarative_base()


class Users(Base):
    __tablename__ = "users2"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    email = Column(String(64))

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value


# 创建session
Base.metadata.create_all(engine)



