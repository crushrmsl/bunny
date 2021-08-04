# -*- coding: utf-8 -*-


import pytest

from data import register_data as rd
from page_objects.register_page import RegisterPage


# 测试用例 = 测试对象的功能 + 测试数据
@pytest.mark.smoke
@pytest.mark.register
@pytest.mark.usefixtures("init_driver")
class TestLogin(object):

    @pytest.mark.register_success
    @pytest.mark.parametrize("data", rd.success_data)
    def test_register_success(self, data, init_driver):

        # 注册
        RegisterPage(init_driver).register_action(data["user"], data["pwd"], data['cpwd'], data['name'],
                                                  data['gender'], data['identity_code'], data['email'], data['mobile'])
        try:
            # 断言
            assert RegisterPage(init_driver).get_success_msg() == "注册成功！"
        except AssertionError as e:
            raise e
        finally:
           pass

    @pytest.mark.register_fail
    @pytest.mark.register_username_wrong
    @pytest.mark.parametrize("data", rd.username_wrong_data)
    def test_register_username_wrong(self, data, init_driver):

        # 注册
        RegisterPage(init_driver).register_action(data["user"], data["pwd"], data['cpwd'], data['name'],
                                                  data['gender'], data['identity_code'], data['email'], data['mobile'])
        try:
            # 断言
            assert RegisterPage(init_driver).get_username_wrong_msg() == '用户名不能为空.'
        except AssertionError as e:
            raise e
        finally:
            pass

    @pytest.mark.register_fail
    @pytest.mark.register_password_wrong
    @pytest.mark.parametrize("data", rd.password_wrong_data)
    def test_login_password_wrong(self, data, init_driver):

        # 注册
        RegisterPage(init_driver).register_action(data["user"], data["pwd"], data['cpwd'], data['name'],
                                                  data['gender'], data['identity_code'], data['email'], data['mobile'])
        try:
            # 断言
            assert RegisterPage(init_driver).get_password_different_msg() == '两次输入的密码不一致.'
        except AssertionError as e:
            raise e
        finally:
            pass

    @pytest.mark.register_fail
    @pytest.mark.register_password_wrong
    @pytest.mark.parametrize("data", rd.username_exists_data)
    def test_login_username_exists(self, data, init_driver):

        # 注册
        RegisterPage(init_driver).register_action(data["user"], data["pwd"], data['cpwd'], data['name'],
                                                  data['gender'], data['identity_code'], data['email'], data['mobile'])

        try:
            # 断言
            assert RegisterPage(init_driver).get_username_exists_msg() == '用户已经存在！'
        except AssertionError as e:
            raise e
        finally:
            pass
