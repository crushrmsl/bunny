# -*- coding: utf-8 -*-


# 登录成功
success_data = [
    {"user": "admin", "pwd": "123456", "name": "系统管理员"},
    {"user": "cgn", "pwd": "123456", "name": "程广宁"},
    {"user": "hyl", "pwd": "123456", "name": "韩语良"}
]

no_username_data = [
    {"user": "", "pwd": "123456"}
]

no_password_data = [
    {"user": "admin", "pwd": ""}
]

username_wrong_data = [
    {"user": "admin100", "pwd": "123456"},
    {"user": "xyz123", "pwd": "123456"}
]

password_wrong_data = [
    {"user": "admin", "pwd": "111111"},
    {"user": "cgn", "pwd": "000000"}
]

