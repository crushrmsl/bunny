# -*- coding: utf-8 -*-


import pytest

from data import login_data as ld
from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage


@pytest.mark.smoke
@pytest.mark.logout
@pytest.mark.usefixtures("init_driver")
class TestLogout(object):

    @pytest.mark.parametrize("data", ld.success_data)
    def test_logout_success(self, data, init_driver):

        # 登录
        LoginPage(init_driver).login_action(data["user"], data["pwd"])

        # 登出
        IndexPage(init_driver).logout_action()


