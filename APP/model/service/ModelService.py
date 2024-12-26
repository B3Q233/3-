from APP.model.operation.ModelsModel import *


# 获取全部AI模型信息，并转换成字典
def get_all_AI():
    ai_list = find_all_ai_models()
    AI_models = []
    for ai in ai_list:
        AI_models.append(ai.to_dict())
    return AI_models


if __name__ == '__main__':
    get_all_AI()
