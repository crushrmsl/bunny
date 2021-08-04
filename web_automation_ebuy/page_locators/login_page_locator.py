# -*- coding: utf-8 -*-


from selenium.webdriver.common.by import By


class LoginPageLocator(object):

    # 登录按钮
    index_login_button_loc = By.XPATH, "//a[text()='登录']"

    # 用户名输入框
    username_input_loc = By.XPATH, "//input[@id='loginName']"

    # 密码输入框
    pwd_input_loc = By.XPATH, By.XPATH, "//input[@class='l_pwd']"

    # 登录按钮
    login_button_loc = By.XPATH, "//input[@type='button']"

    # 用户名不存在提示信息
    no_username_msg_loc = By.XPATH, "//span[text()='用户不存在！']"

    # 密码错误提示信息
    password_wrong_msg_loc = By.XPATH, "//span[text()='密码错误！']"

    # 关闭提示信息按钮
    close_msg_button_loc = By.XPATH, "//img[@src='/ebuy/statics/images/close.gif']"

