# -*- coding: utf-8 -*-
import os
import sys
import pytest

from data import login_data as ld
from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage


# 测试用例 = 测试对象的功能 + 测试数据
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.usefixtures("init_driver")
class TestLogin(object):

    @pytest.mark.login_success
    @pytest.mark.parametrize("data", ld.success_data)
    def test_login_success(self, data, init_driver):

        # 登录
        LoginPage(init_driver).login_action(data["user"], data["pwd"])

        try:
            # 断言
            assert LoginPage(init_driver).get_index_username() == data['name']
        except AssertionError as e:
            raise e
        finally:
            # 登出
            IndexPage(init_driver).logout_action()

    @pytest.mark.login_username_wrong
    @pytest.mark.parametrize("data", ld.no_username_data)
    def test_login_no_username(self, data, init_driver):

        # 登录
        LoginPage(init_driver).login_action(data["user"], data["pwd"])

        try:
            # 断言
            assert LoginPage(init_driver).get_no_username_msg() == '用户名不能为空！'
        except AssertionError as e:
            raise e
        finally:
            IndexPage(init_driver).logout_action()

    @pytest.mark.login_username_wrong
    @pytest.mark.parametrize("data", ld.no_password_data)
    def test_login_no_password(self, data, init_driver):

        # 登录
        LoginPage(init_driver).login_action(data["user"], data["pwd"])

        try:
            # 断言
            assert LoginPage(init_driver).get_password_wrong_msg() == '密码错误！'
        except AssertionError as e:
            raise e
        finally:
            pass

    @pytest.mark.login_username_wrong
    @pytest.mark.parametrize("data", ld.username_wrong_data)
    def test_login_username_wrong(self, data, init_driver):

        # 登录
        LoginPage(init_driver).login_action(data["user"], data["pwd"])

        try:
            # 断言
            assert LoginPage(init_driver).get_no_username_msg() == '用户不存在！'
        except AssertionError as e:
            raise e
        finally:
            pass

    @pytest.mark.parametrize("data", ld.password_wrong_data)
    def test_login_password_wrong(self, data, init_driver):

        # 登录
        LoginPage(init_driver).login_action(data["user"], data["pwd"])

        try:
            # 断言
            assert LoginPage(init_driver).get_password_wrong_msg() == '密码错误！'
        except AssertionError as e:
            raise e
        finally:
            pass
