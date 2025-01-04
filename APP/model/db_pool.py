import configparser
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

engine = None

Base = declarative_base()


def init():
    global engine

    config = configparser.ConfigParser()
    config_file_path = os.path.join(os.path.dirname(__file__), 'db.ini')
    config.read(config_file_path)

    db_config = config['database']
    pool_config = config['pool']

    connection_string = (
        f"{db_config['driver_name']}+pymysql://{db_config['user']}:{db_config['password']}@"
        f"{db_config['host']}:{db_config['port']}/{db_config['name']}"
    )

    print(connection_string)

    engine = create_engine(
        connection_string,
        pool_size=int(pool_config['pool_size']),
        max_overflow=int(pool_config['max_overflow']),
        pool_timeout=int(pool_config['pool_timeout']),
        pool_recycle=int(pool_config['pool_recycle']),
    )


    global Session,Base
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)


def get_session():
    """
    获取数据库连接的函数（返回Session实例）
    """
    return Session()


def close_session(session):
    """
    关闭Session实例的函数
    """
    session.close()


init()


