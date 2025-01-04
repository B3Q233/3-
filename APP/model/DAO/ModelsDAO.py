import time
from APP.logs.logConfig import logging
from APP.model.db_pool import get_session
from APP.model.entity.Model import *

# 配置日志记录器
current_time = time.strftime('%Y-%m-%d', time.localtime())
logging.basicConfig(
    level=logging.ERROR,  # 设置日志级别为ERROR，只记录错误信息
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a'  # 追加模式，每次记录日志在文件末尾添加
)


def delete_model_by_id(model_id):
    """
        根据模型id删除数据库中的模型
    """
    session = get_session()
    try:
        model = session.query(Model).filter(Model.model_id == model_id).first()
        if model:
            session.delete(model)
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        session.rollback()
        logging.error(f"在删除模型时出现错误，模型ID: {model_id}，错误信息: {e}", exc_info=True)
        return False
    finally:
        session.close()


def find_all_ai_models():
    """
        查询数据库中所有的AI模型信息
    """
    session = get_session()
    try:
        models = session.query(Model).all()
        return models
    except Exception as e:
        logging.error(f"在查询所有AI模型信息时出现错误，错误信息: {e}", exc_info=True)
    finally:
        session.close()


def insert_model(new_model):
    """
        插入新模型信息到数据库
    """
    session = get_session()
    try:
        session.add(new_model)
        session.commit()
    except Exception as e:
        logging.error(f"在插入新模型信息时出现错误，模型信息: {new_model}，错误信息: {e}", exc_info=True)
        session.rollback()
        raise
    finally:
        session.close()


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


def update_whole_model(new_model):
    """
       修改模型
    """
    session = get_session()
    try:
        model = session.query(Model).filter(Model.model_id == new_model.model_id).first()
        if model:
            model.model_name = new_model.model_name
            model.model_category = new_model.model_category
            model.model_description = new_model.model_description
            model.initial_text = new_model.initial_text
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        logging.error(f"在更新模型的所有信息时出现错误，错误信息: {e}", exc_info=True)
    finally:
        session.close()


if __name__ == '__main__':
    modify_model(
        Model(model_id=4, model_name='b3q123', model_category='fasd', initial_text='12312', model_description='12312'))

    pass
