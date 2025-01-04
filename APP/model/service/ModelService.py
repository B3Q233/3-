from APP.model.DAO import ModelsDAO
from APP.model.entity.UserModelUsage import *


# 获取全部AI模型信息，并转换成字典
def get_all_AI():
    ai_list = ModelsDAO.find_all_ai_models()
    AI_models = []
    for ai in ai_list:
        AI_models.append(ai.to_dict())
    return AI_models


# 模型删除
def model_delete(model_id):
    status = ModelsDAO.delete_model_by_id(model_id)
    if status:
        return '删除成功', status
    else:
        return '删除失败，对应的模型不存在', status
    pass


# 模型添加
def model_add(new_model):
    if new_model.model_name is None \
            or new_model.model_category is None \
            or new_model.initial_text is None \
            or new_model.model_description is None:
        return '新模型参数填写错误，请重新输入', False
    if ModelsDAO.find_model_by_name(new_model.model_name) is not None:
        return '模型名重复，请重新输入', False
    ModelsDAO.insert_model(new_model)
    return '添加模型名成功', True


def get_model_by_id(model_id):
    get_model = ModelsDAO.find_model_by_id(model_id)
    if get_model is None:
        return '模型不存在', False
    return get_model.to_dict(), True


def whole_model_update(new_model):
    found_model = ModelsDAO.find_model_by_name(new_model.model_name)
    if found_model is not None:
        if found_model.model_name != new_model.model_name:
            return '模型名重复，请重新填写', False
    status = ModelsDAO.update_whole_model(new_model)
    if not status:
        return '模型更新失败', False
    else:
        return '模型更新成功', True


if __name__ == '__main__':
    print(get_model_by_id(5))
