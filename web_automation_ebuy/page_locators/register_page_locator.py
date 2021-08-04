# -*- coding: utf-8 -*-


from selenium.webdriver.common.by import By


class RegisterPageLocator(object):

    # 免费注册按钮
    index_register_button_loc = By.XPATH, "//a[text()='免费注册']"

    # 用户名输入框
    username_input_loc = By.XPATH, "//input[@name='loginName']"

    # 性别男
    male_loc = By.XPATH, "//input[@value='1']"

    # 性别女
    female_loc = By.XPATH, "//input[@value='0']"

    # 身份证输入框
    identity_code_input_loc = By.XPATH, "//input[@name='identityCode']"

    # 邮箱
    email_input_loc = By.XPATH, "//input[@name='email']"

    # 手机输入框
    mobile_input_loc = By.XPATH, "//input[@name='mobile']"

    # 注册按钮
    register_button_loc = By.XPATH, "//input[@type='button']"

    # 注册成功提示语
    register_success_loc = By.XPATH, "//span[text()='注册成功！']"

    # 用户名已存在提示语
    username_exists_msg_loc = By.XPATH, "//span[text()='用户已经存在！']"

    # 用户名不能为空提示信息
    no_username_msg_loc = By.XPATH, "//span[text()='用户名不能为空.']"

    # 密码不能为空提示信息
    no_password_msg_loc = By.XPATH, "//span[text()='密码不能为空']"

    # 两次密码不一致提示信息
    password_different_msg_loc = By.XPATH, "//span[text()='两次输入的密码不一致.']"

    # 真实姓名不能为空提示信息
    no_true_name_msg_loc = By.XPATH, "//span[text()='真实姓名不能为空.']"

    # 关闭提示信息按钮
    close_msg_button_loc = By.XPATH, "//img[@src='/ebuy/statics/images/close.gif']"




