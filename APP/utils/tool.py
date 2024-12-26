import re

# 正则表达式常量
NAME_REGEX = r"^[a-zA-Z]{3,}$"
PASSWORD_REGEX = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,12}$"
EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


# 验证函数
def validate_name(username):
    return re.match(NAME_REGEX, username) is not None


def validate_password(password):
    return re.match(PASSWORD_REGEX, password) is not None


def validate_email(email):
    return re.match(EMAIL_REGEX, email) is not None
