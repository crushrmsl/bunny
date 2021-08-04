# -*- coding: utf-8 -*-


from selenium.webdriver.common.by import By


class IndexPageLocator(object):

    # 用户名称
    username_loc = By.XPATH, "//a[@href='/ebuy/admin/user?action=index']"

    # 注销按钮
    logout_button_loc = By.XPATH, "//a[text()='注销']"


