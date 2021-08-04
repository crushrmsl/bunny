# -*- coding: utf-8 -*-


import time

from common.basepage import BasePage
from page_locators.index_page_locator import IndexPageLocator as Loc


class IndexPage(BasePage):

    def logout_action(self):
        self.click_element(loc=Loc.logout_button_loc, img_desc="首页-退出登录按钮")
        time.sleep(1)
