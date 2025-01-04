import os
import ast
import json
from zhipuai import ZhipuAI
from APP.model.service import UserModelUsageService, UserService
from APP.utils.tool import parse_data
from APP.model.service.ModelService import UserModelUsage


client = ZhipuAI(api_key="e7d7fe0a829e0872b438334405c37a8c.xRof5ICQsaRtFf6u")  # 使用您自己的APIKey

saved_msg = {}


def getImgResponse(prompt, model_category):
    print(prompt)
    try:
        response = client.images.generations(
            model=model_category,
            prompt=prompt,
        )
        return response.data[0].url
    except Exception as e:
        # 记录异常信息，这里简单打印，实际应用中可记录到日志文件等
        print(f"图像生成请求出现异常: {e}")
        return None


def getResponse(msg, model_category):
    try:
        response = client.chat.completions.create(
            model=model_category,
            messages=msg,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"文本生成请求出现异常: {e}")
        return None


def database_handle(user_id, model_id, msg, model_category):
    try:
        # 更新用户配额
        rt_msg, status = UserService.update_user_quota(user_id, -5)
        if not status:
            return json.dumps({'status': 0, 'msg': rt_msg})

        # 获取使用历史记录
        ret_history = UserModelUsageService.get_usage_history(user_id, model_id)
        usage_content = ast.literal_eval(ret_history['usage_content'])
        usage_content.append({'role': 'user', 'content': msg})

        # 获取AI回复
        ret_msg = getResponse(usage_content, model_category)
        usage_content.append({'role': 'system', 'content': ret_msg})

        # 更新数据库中的使用记录
        UserModelUsageService.update_usage(UserModelUsage(user_id=user_id, model_id=model_id, usage_content=str(usage_content)))
        return json.dumps({'status': 1, 'msg': ret_msg})
    except (ValueError, KeyError) as e:
        print(f"数据库操作相关异常: {e}")
        return json.dumps({'status': 0, 'msg': '数据库操作出现问题，请稍后再试'})
    except Exception as e:
        print(f"其他异常: {e}")
        return json.dumps({'status': 0, 'msg': '处理过程出现未知错误，请联系管理员'})


def _init_user_msg(user_id, model_id, model_description):
    if user_id not in saved_msg:
        saved_msg[user_id] = {}
    if saved_msg.get(user_id).get(model_id) is None:
        saved_msg[user_id][model_id] = []
        saved_msg[user_id][model_id].append({'role': 'system', 'content': model_description})


def _insert_usage_and_reset(user_id, model_id):
    new_usage = UserModelUsage(user_id=user_id, model_id=model_id, usage_content=str(saved_msg[user_id][model_id]))
    UserModelUsageService.insert_usage(new_usage)
    saved_msg[user_id][model_id] = [-1]


def get_user_msg(request):
    try:
        data = parse_data(request)
        user_id = data.get('user_id')[0]
        model_str = data.get('model')[0]
        model = json.loads(model_str)
        model_id = model['model_id']
        model_category = model['model_category']
        model_description = model['model_description']
        get_msg = data.get('msg')[0]

        # 初始化用户消息记录
        _init_user_msg(user_id, model_id, model_description)

        # 根据不同情况处理消息
        if model_category!= 'cogview-3-flash' and len(saved_msg[user_id][model_id]) >= 1 and saved_msg[user_id][model_id][0] == -1:
            return database_handle(user_id, model_id, get_msg, model_category)
        else:
            saved_msg[user_id][model_id].append({'role': 'user', 'content': get_msg})
            if model_category == 'cogview-3-flash':
                msg, status = UserService.update_user_quota(user_id, -10)
                if status:
                    ret_msg = getImgResponse(prompt=get_msg, model_category=model_category)
                    ret_msg = [{'url': ret_msg}] if ret_msg else []
                else:
                    ret_msg = msg
                    return json.dumps({'status': 0, 'msg': ret_msg})
            else:
                msg, status = UserService.update_user_quota(user_id, -5)
                if status:
                    ret_msg = getResponse(saved_msg[user_id][model_id], model_category)
                    saved_msg[user_id][model_id].append({'role': 'system', 'content': ret_msg})
                else:
                    ret_msg = msg
                    return json.dumps({'status': 0, 'msg': ret_msg})

            # 处理消息记录长度达到上限的情况
            if model_category!= 'cogview-3-flash' and len(saved_msg[user_id][model_id]) >= 20:
                _insert_usage_and_reset(user_id, model_id)
            return json.dumps({'status': 1, 'msg': ret_msg})
    except Exception as e:
        print(f"处理用户消息出现异常: {e}")
        return json.dumps({'status': 0, 'msg': '处理用户消息时出现错误，请稍后再试'})


def get_ai_response(msg):
    if isinstance(msg, bytes):
        string = msg.decode('utf-8')
    else:
        string = msg
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
        try:
            data['msg'] = input("请输入消息（输入 'exit' 可退出）: ")
            if data['msg'].lower() == 'exit':
                break
            result = get_user_msg(data=data)
            print(json.loads(result)['msg'])
        except Exception as e:
            print(f"主程序交互出现异常: {e}")