# -*- coding: utf-8 -*-


import pytest
from selenium import webdriver
from data import common_data as cd


# 声明以下的函数是pytest的前置后置
# 每条用例执行完成后会退出浏览器
@pytest.fixture(scope='session')
def init_driver():
    # 启动参数
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(cd.login_url)
    yield driver
    driver.quit()


