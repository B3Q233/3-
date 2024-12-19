import time
from APP.model.entity.Model import Model
from APP.logs.logConfig import logging
from APP.model.sqltest import get_session

# 配置日志记录器
current_time = time.strftime('%Y-%m-%d', time.localtime())
logging.basicConfig(
    level=logging.ERROR,  # 设置日志级别为ERROR，只记录错误信息
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a'  # 追加模式，每次记录日志在文件末尾添加
)


def find_model_by_id(model_id):
    """
    根据模型id查找大模型信息
    """
    session = get_session()
    try:
        model = session.query(Model).filter(Model.model_id == model_id).first()
        return model
    except Exception as e:
        logging.error(f"在根据模型id查找大模型信息时出现错误，模型id: {model_id}，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def find_model_by_name(model_name):
    """
    根据模型名称查找大模型信息
    """
    session = get_session()
    try:
        model = session.query(Model).filter(Model.model_name == model_name).first()
        return model
    except Exception as e:
        logging.error(f"在根据模型名称查找大模型信息时出现错误，模型名称: {model_name}，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def find_model_by_category(model_category):
    """
    根据模型类别查找大模型信息
    """
    session = get_session()
    try:
        model = session.query(Model).filter(Model.model_category == model_category).first()
        return model
    except Exception as e:
        logging.error(f"在根据模型类别查找大模型信息时出现错误，模型类别: {model_category}，错误信息: {e}", exc_info=True)
    finally:
        session.close()
