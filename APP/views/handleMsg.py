import json
from APP.utils.tool import *
from zhipuai import ZhipuAI
from flask import session

client = ZhipuAI(api_key="e7d7fe0a829e0872b438334405c37a8c.xRof5ICQsaRtFf6u")  # 使用您自己的APIKey
saved_msg = {}


def getResponse(msg, model_category):
    response = client.chat.completions.create(
        model=model_category,  # 使用您需要调用的模型编码
        messages=msg,
    )
    retStr = response.choices[0].message.content
    return retStr


def get_user_msg(request, data, user_id):
    # data = parse_data(request)
    user_id = user_id
    model_id = data.get('model').get('model_id')
    model_category = data.get('model').get('model_category')
    model_description = data.get('model').get('model_description')
    msg = data.get('msg')
    if user_id not in saved_msg:
        saved_msg[user_id] = {}
    if saved_msg.get(user_id).get(model_id) is None:
        saved_msg[user_id][model_id] = []
        saved_msg[user_id][model_id].append({'role': 'system', 'content': model_description})
        saved_msg[user_id][model_id].append({'role': 'user', 'content': msg})
    else:
        saved_msg[user_id][model_id].append({'role': 'user', 'content': msg})
    print(saved_msg[user_id][model_id])
    ret_msg = getResponse(saved_msg[user_id][model_id], model_category)
    saved_msg[user_id][model_id].append({'role': 'system', 'content': ret_msg})
    print(ret_msg)
    pass


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
        'msg': '你好，哥哥',
        'model': {
            "model_id": 1,
            "model_name": "蔡徐坤",
            "model_category": "glm-4-plus",
            "initial_text": "你好，我是cxk",
            "model_description": "会唱跳rap的聊天机器人"
        }
    }
    while True:
        user_id = int(input())
        data['msg'] = input()
        get_user_msg(request="123", data=data, user_id=user_id)
