import json

from zhipuai import ZhipuAI

client = ZhipuAI(api_key="e7d7fe0a829e0872b438334405c37a8c.xRof5ICQsaRtFf6u")  # 使用您自己的APIKey

messages = []


def getResponse(msg):
    messages.append({"role": "user", "content": msg})
    response = client.chat.completions.create(
        request_id='20241215233705728d38ee23f147de',
        model="glm-4-0520",  # 使用您需要调用的模型编码
        messages=messages,
    )
    with open('response.json', 'w') as f:
        json.dump(response.to_json(), f)
    retStr = response.choices[0].message.content
    messages.append({"role": "assistant", "content": retStr})
    with open('response.json', 'w') as f:
        json.dump(messages, f)
    return retStr


def AIResponse(msg):
    # 检查msg是否为字节类型，如果是，则解码为字符串
    if isinstance(msg, bytes):
        string = msg.decode('utf-8')
    else:
        string = msg
    # 使用传入的msg参数调用getResponse函数
    return getResponse(string)
