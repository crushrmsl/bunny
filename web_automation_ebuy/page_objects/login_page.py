# -*- coding: utf-8 -*-


import time

from common.basepage import BasePage
from page_locators.login_page_locator import LoginPageLocator as Loc
from page_locators.index_page_locator import IndexPageLocator as Ioc


class LoginPage(BasePage):

    def login_action(self, username, pwd):
        time.sleep(1)
        self.click_element(loc=Loc.index_login_button_loc, img_desc="登录页面_右上方登录按钮")

        self.input_two_text(loc=Loc.username_input_loc, value1=username, value2=pwd, img_desc="登录页面_用户名密码输入框")
        self.click_element(loc=Loc.login_button_loc, img_desc="登录页面_登录按钮")
        time.sleep(1)

    # 断言是否登录成功 只有登录成功 页面右上角才会显示 系统管理员
    def get_index_username(self):
        text = self.get_text(loc=Ioc.username_loc, img_desc='首页-用户名')
        return text

    # 获取登录时用户名不存在的提示信息
    def get_no_username_msg(self):
        text = self.get_text(loc=Loc.no_username_msg_loc, img_desc="登录页-用户名不存在提示信息")
        self.click_element(loc=Loc.close_msg_button_loc, img_desc="登录页-提示信息关闭按钮")
        return text

    # 获取登录时用户名不存在的提示信息
    def get_no_password_msg(self):
        text = self.get_text(loc=Loc.password_wrong_msg_loc, img_desc="登录页-密码错误提示信息")
        self.click_element(loc=Loc.close_msg_button_loc, img_desc="登录页-提示信息关闭按钮")
        return text

    # 获取登录时用户名不存在的提示信息
    def get_no_username_or_password_msg(self):
        text = self.get_text(loc=Loc.password_wrong_msg_loc, img_desc="登录页-用户名或密码不输入提示信息")
        self.click_element(loc=Loc.close_msg_button_loc, img_desc="登录页-提示信息关闭按钮")
        return text

    # 获取登录时密码错误的提示信息
    def get_password_wrong_msg(self):
        text = self.get_text(loc=Loc.password_wrong_msg_loc, img_desc="登录页-密码错误提示信息")
        self.click_element(loc=Loc.close_msg_button_loc, img_desc="登录页-提示信息关闭按钮")
        return text
