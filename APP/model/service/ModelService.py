from APP.model.operation import ModelsModel
from APP.model.entity.Model import *


# 获取全部AI模型信息，并转换成字典
def get_all_AI():
    ai_list = ModelsModel.find_all_ai_models()
    AI_models = []
    for ai in ai_list:
        AI_models.append(ai.to_dict())
    return AI_models


# 模型删除
def model_delete(model_id):
    status = ModelsModel.delete_model_by_id(model_id)
    if status:
        return '删除成功',status
    else:
        return '删除失败，对应的模型不存在',status
    pass


# 模型添加
def model_add(new_model):
    if new_model.model_name is None \
            or new_model.model_category is None \
            or new_model.initial_text is None \
            or new_model.model_description is None:
        return '新模型参数填写错误，请重新输入', False
    if ModelsModel.find_model_by_name(new_model.model_name) is not None:
        return '模型名重复，请重新输入', False
    ModelsModel.insert_model(new_model)
    return '添加模型名成功', True


if __name__ == '__main__':
    print(model_delete(4))