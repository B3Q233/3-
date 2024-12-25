import json

from zhipuai import ZhipuAI

client = ZhipuAI(api_key="e7d7fe0a829e0872b438334405c37a8c.xRof5ICQsaRtFf6u")  # 使用您自己的APIKey


def getResponse(msg):
    response = client.chat.completions.create(
        model="glm-4-0520",  # 使用您需要调用的模型编码
        messages=[
            {"role": "system", "content": '你是一位程序编写大师'},
            {"role": "user", "content": msg},
        ],
    )
    retStr = response.choices[0].message.content
    return retStr


def AIResponse(msg):
    # 检查msg是否为字节类型，如果是，则解码为字符串
    if isinstance(msg, bytes):
        string = msg.decode('utf-8')
    else:
        string = msg
    # 使用传入的msg参数调用getResponse函数
    return getResponse(string)


if __name__ == '__main__':
    print(getResponse('能简单解释一下原神服务器的原理吗？'))
