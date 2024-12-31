import ast
import json

from zhipuai import ZhipuAI

from APP.model.service import UserModelUsageService
from APP.utils.tool import parse_data

from APP.model.service.ModelService import *

client = ZhipuAI(api_key="e7d7fe0a829e0872b438334405c37a8c.xRof5ICQsaRtFf6u")  # 使用您自己的APIKey
saved_msg = {}


def getImgResponse(prompt, model_category):
    response = client.images.generations(
        model=model_category,  # 填写需要调用的模型编码
        prompt=prompt,
    )
    return response.data[0].url


def getResponse(msg, model_category):
    response = client.chat.completions.create(
        model=model_category,  # 使用您需要调用的模型编码
        messages=msg,
    )
    retStr = response.choices[0].message.content
    return retStr


def database_handle(user_id, model_id,msg,model_category):
    ret_history = UserModelUsageService.get_usage_history(user_id, model_id)
    usage_content = ast.literal_eval(ret_history['usage_content'])
    print(type(usage_content))
    usage_content.append({'role': 'user', 'content': msg})
    ret_msg = getResponse(usage_content,model_category)
    usage_content.append({'role': 'system', 'content': ret_msg})
    UserModelUsageService.update_usage(UserModelUsage(user_id=user_id,model_id=model_id, usage_content=str(usage_content)))
    return json.dumps({'status': 1, 'msg': ret_msg})


def get_user_msg(request):
    data = parse_data(request)
    user_id = data.get('user_id')[0]
    model_str = data.get('model')[0]  # 获取 model 字符串
    model = json.loads(model_str)  # 将 model 字符串转换为字典
    model_id = model['model_id']
    model_category = model['model_category']
    model_description = model['model_description']
    msg = data.get('msg')[0]
    if user_id not in saved_msg:
        saved_msg[user_id] = {}
    if saved_msg.get(user_id).get(model_id) is None:
        saved_msg[user_id][model_id] = []
        saved_msg[user_id][model_id].append({'role': 'system', 'content': model_description})
        saved_msg[user_id][model_id].append({'role': 'user', 'content': msg})
    elif model_category != 'cogview-3-flash' and len(saved_msg[user_id][model_id]) >= 1 and saved_msg[user_id][model_id][0] == -1:
        return database_handle(user_id, model_id,msg,model_category)
    else:
        saved_msg[user_id][model_id].append({'role': 'user', 'content': msg})
    if model_category == 'cogview-3-flash':
        ret_msg = getImgResponse(prompt=msg, model_category=model_category)
        ret_msg = [{'url': ret_msg}]
    else:
        ret_msg = getResponse(saved_msg[user_id][model_id], model_category)
        saved_msg[user_id][model_id].append({'role': 'system', 'content': ret_msg})
    if model_category != 'cogview-3-flash' and len(saved_msg[user_id][model_id]) >= 20:
        new_usage = UserModelUsage(user_id=user_id, model_id=model_id, usage_content=str(saved_msg[user_id][model_id]))
        UserModelUsageService.insert_usage(new_usage)
        saved_msg[user_id][model_id] = [-1]
    return json.dumps({'status': 1, 'msg': ret_msg})


def get_ai_response(msg):
    # 检查msg是否为字节类型，如果是，则解码为字符串
    if isinstance(msg, bytes):
        string = msg.decode('utf-8')
    else:
        string = msg
    # 使用传入的msg参数调用getResponse函数
    return getResponse(string)


if __name__ == '__main__':
    data = {
        'user_id': [1, 2],
        'msg': '你好，哥哥',
        'model': [{
            "model_id": 1,
            "model_name": "蔡徐坤",
            "model_category": "glm-4-plus",
            "initial_text": "你好，我是cxk",
            "model_description": "会唱跳rap的聊天机器人"
        }]
    }
    while True:
        data['msg'] = input()
        get_user_msg(data=data)
