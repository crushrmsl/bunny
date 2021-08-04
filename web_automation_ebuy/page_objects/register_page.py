# -*- coding: utf-8 -*-


import time

from common.basepage import BasePage
from page_locators.register_page_locator import RegisterPageLocator as Roc
from page_locators.index_page_locator import IndexPageLocator as Ioc


class RegisterPage(BasePage):

    def register_action(self, username, pwd, cpwd, name, gender, identity_code, email, mobile):
        time.sleep(1)
        self.click_element(loc=Roc.index_register_button_loc, img_desc="登录页面_右上方免费注册按钮")

        self.input_four_text(loc=Roc.username_input_loc, value1=username, value2=pwd, value3=cpwd, value4=name, img_desc="注册页面_用户名密码输入框")
        if gender == 'male':
            self.click_element(Roc.male_loc, img_desc="注册页-性别男")
        else:
            self.click_element(Roc.female_loc, img_desc="注册页-性别女")

        self.input_text(loc=Roc.identity_code_input_loc, value=identity_code, img_desc="注册页-身份证输入框")
        self.input_text(loc=Roc.email_input_loc, value=email, img_desc="注册页-邮箱输入框")
        self.input_text(loc=Roc.mobile_input_loc, value=mobile, img_desc="注册页-手机号输入框")

        self.click_element(loc=Roc.register_button_loc, img_desc="注册页面_注册按钮")
        time.sleep(1)

    # 获取注册成功提示语
    def get_success_msg(self):
        text = self.get_text(loc=Roc.register_success_loc, img_desc='注册页-注册成功提示信息')
        self.click_element(loc=Roc.close_msg_button_loc, img_desc="注册页-提示信息关闭按钮")
        return text

    # 获取-用户名不能为空的提示信息
    def get_username_wrong_msg(self):
        text = self.get_text(loc=Roc.no_username_msg_loc, img_desc="注册页-用户名不能为空")
        self.click_element(loc=Roc.close_msg_button_loc, img_desc="注册页-提示信息关闭按钮")
        return text

    # 获取-密码不能为空的提示信息
    def get_password_different_msg(self):
        text = self.get_text(loc=Roc.password_different_msg_loc, img_desc="注册页-两次输入的密码不一致")
        self.click_element(loc=Roc.close_msg_button_loc, img_desc="注册页-提示信息关闭按钮")
        return text

    # 获取-密码不能为空的提示信息
    def get_username_exists_msg(self):
        text = self.get_text(loc=Roc.username_exists_msg_loc, img_desc="注册页-用户已经存在")
        self.click_element(loc=Roc.close_msg_button_loc, img_desc="注册页-提示信息关闭按钮")
        return text
