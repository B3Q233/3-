import unittest
from APP.control.AI_model.AI_ask_handle import get_user_msg


class TestGetUserMsg(unittest.TestCase):
    def setUp(self):
        self.data = {
            "user_id": [4],
            "model": [
                "{\"model_id\": 8, \"model_category\": \"glm-4-plus\", \"model_description\": \"good boy\"}"],
            "msg": ["test message"]
        }

    def set_msg(self, msg):
        self.data = {
            "user_id": [4],
            "model": [
                "{\"model_id\": 8, \"model_category\": \"glm-4-plus\", \"model_description\": \"good boy\"}"],
            "msg": [msg]
        }

    def test_get_user_msg(self):
        while True:
            msg = input()
            self.set_msg(msg)
            result = get_user_msg(self.data)
            print(result)
        # self.assertEqual(isinstance(result, str), True)  # 验证返回结果是字符串类型（因为最后返回的是json.dumps后的结果）


if __name__ == '__main__':
    unittest.main()
