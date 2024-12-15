from zhipuai import ZhipuAI
client = ZhipuAI(api_key="e7d7fe0a829e0872b438334405c37a8c.xRof5ICQsaRtFf6u") # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4-0520",  # 填写需要调用的模型编码
    messages=[
        {"role": "user", "content": "说明一下mvc架构"},
    ],
)
print(response.choices[0].message.content)