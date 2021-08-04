# -*- coding: utf-8 -*-


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import datetime

from common.constant import SCREENSHOT_DIR
from common.logger import output_log


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, loc, img_desc, timeout=30, frequency=0.5):
        start = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(ec.visibility_of_element_located(loc))
        except:
            # 日志
            output_log.exception(f"等待 {img_desc} 元素 {loc} 可见失败！")
            # 截图
            self.save_img(img_desc)
            # 抛出异常 让框架识别用例失败
            raise
        else:
            end = datetime.datetime.now()
            output_log.info(f"等待 {img_desc} 元素 {loc} 可见成功, 耗时: {end - start}")

    # 等待元素存在
    def wait_ele_exists(self, loc, img_desc, timeout=30, frequency=0.5):
        start = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(ec.presence_of_element_located(loc))
        except:
            # 日志
            output_log.exception(f"等待 {img_desc} 元素 {loc} 存在失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            end = datetime.datetime.now()
            output_log.info(f"等待 {img_desc} 元素 {loc} 存在成功, 耗时: {end - start}")

    # 查找元素
    def get_element(self, loc, img_desc, find_all=False):
        """
        :param loc: 元组类型。元素定位表达式: (定位类型,定位表达式)
        :param img_desc: 截图命名
        :param find_all: 是否查找所有匹配的元素。为False表示只匹配一个。为True表示获取匹配所有。
        :return: Webelement对象。当find_all为True时，返回的是列表。
        """
        try:
            if find_all is True:
                ele = self.driver.find_elements(*loc)
            else:
                ele = self.driver.find_element(*loc)
        except:
            # 日志
            output_log.exception(f"查找 {img_desc} 元素 {loc} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"查找 {img_desc} 元素 {loc} 成功！")
            return ele

    # 元素可以是通过元素定位查找，也可以是直接是webElement对象。
    def _deal_element(self, loc, img_desc, timeout=30, frequency=0.5, wait_type="visible"):
        if isinstance(loc, str):
            # 处理一下 可接收字符串的元组
            loc = eval(loc)
        # 先等待可见,再查找元素
        if isinstance(loc, tuple):  # 元素定位表达式类型
            if wait_type == "visible":  # 等待元素可见
                self.wait_ele_visible(loc, img_desc, timeout, frequency)
            else:  # 等待元素存在
                self.wait_ele_exists(loc, img_desc, timeout, frequency)
            return self.get_element(loc, img_desc)
        # WebElement对象
        elif isinstance(loc, WebElement):
            return loc
        else:
            output_log.error(f"参数loc: {loc} 即不是元组，也不是WebElement对象，无法根据此参数找到元素")
            raise

    # 点击元素
    def click_element(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        time.sleep(1)
        try:
            ele.click()
        except:
            # 日志
            output_log.exception(f"点击 {img_desc} 元素 {loc} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"点击 {img_desc} 元素 {loc} 成功！")
        return self.driver

    # 清除文本
    def clean_element_text(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        time.sleep(1)
        try:
            ele.clear()
        except:
            # 日志
            output_log.exception(f"清除 {img_desc} 元素 的文本 {loc} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"清除 {img_desc} 元素 的文本 {loc} 成功！")

    def input_text(self, loc, value, img_desc, timeout=30, frequency=0.5, wait_type="visible"):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type)
        time.sleep(1)
        try:
            ele.send_keys(value)
        except:
            # 日志
            output_log.exception(f"在 {img_desc} 元素 {loc} 上输入文本值：{value} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"在 {img_desc} 元素 {loc} 上输入文本值：{value} 成功！")

    def input_two_text(self, loc, value1, value2, img_desc, timeout=30, frequency=0.5, wait_type="visible"):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type)
        time.sleep(1)
        try:
            ele.send_keys(value1, Keys.TAB, value2)
        except:
            # 日志
            output_log.exception(f"在 {img_desc} 元素 {loc} 上输入文本值：{value1} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"在 {img_desc} 元素 {loc} 上输入文本值：{value1} 成功！")

    def input_four_text(self, loc, value1, value2, value3, value4, img_desc, timeout=30, frequency=0.5, wait_type="visible"):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type)
        time.sleep(1)
        try:
            ele.send_keys(value1, Keys.TAB, value2, Keys.TAB, value3, Keys.TAB, value4)
        except:
            # 日志
            output_log.exception(f"在 {img_desc} 元素 {loc} 上输入文本值：{value1} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"在 {img_desc} 元素 {loc} 上输入文本值：{value1} 成功！")

    # 双击元素
    def double_click_element(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        time.sleep(1)
        try:
            # 双击操作
            ActionChains(self.driver).double_click(ele).perform()
        except:
            # 日志
            output_log.exception(f"双击 {img_desc} 元素 {loc} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"双击 {img_desc} 元素 {loc} 成功！")

    # 鼠标悬浮到元素上
    def mouse_move_to_element(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        time.sleep(1)
        try:
            ActionChains(self.driver).move_to_element(ele).perform()
        except:
            # 日志
            output_log.exception(f"悬浮到 {img_desc} 元素 {loc} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"悬浮到 {img_desc} 元素 {loc} 成功！")

    # 滑动要元素底部
    def scroll_to_element_down(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        time.sleep(1)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
        except:
            # 日志
            output_log.exception(f"滑动到 {img_desc} 元素 {loc} 底部 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"滑动到 {img_desc} 元素 {loc} 底部 成功！")

    # 滑动要页面底部
    def scroll_to_page_down(self, img_desc):
        time.sleep(1)
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight); ")
        except:
            # 日志
            output_log.exception(f"滑动到 {img_desc} 底部 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"滑动到 {img_desc} 底部 成功！")

    # 滑动到页面顶部
    def scroll_to_page_up(self, img_desc):
        time.sleep(1)
        try:
            self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0); ")
        except:
            # 日志
            output_log.exception(f"滑动到 {img_desc} 顶部 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"滑动到 {img_desc} 顶部 成功！")
            time.sleep(1)

    # 获取元素的属性值
    def get_element_attribute(self, loc, attr_name, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type="presence")
        try:
            attr_value = ele.get_attribute(attr_name)
        except:
            # 日志
            output_log.exception(f"获取 {img_desc} 元素 {loc} 的属性 {attr_name} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"获取 {img_desc} 元素 {loc} 的属性 {attr_name} 值为:{attr_value}")
            return attr_value

    # 获取元素的css样式中的某项的值 比如 color size等
    def get_element_css_property(self, loc, property, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency)
        try:
            value = ele.value_of_css_property(property)
        except:
            # 日志
            output_log.exception(f"获取 {img_desc} 元素 {loc} 的css {property} 失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"获取 {img_desc} 元素 {loc} 的css {property} 值为:{value}")
            return value

    # 获取元素的文本值。
    def get_text(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type="presence")
        time.sleep(1)
        try:
            text = ele.text
        except:
            # 日志
            output_log.exception(f"获取 {img_desc} 元素 {loc} 的文本失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"获取 {img_desc} 元素 {loc} 的文本值为:{text}")
            return text

    # 获取隐藏元素的文本值。
    def get_hide_text(self, loc, img_desc, timeout=30, frequency=0.5):
        ele = self._deal_element(loc, img_desc, timeout, frequency, wait_type="presence")
        try:
            text = ele.get_attribute("textContent")
        except:
            # 日志
            output_log.exception(f"获取 {img_desc} 元素 {loc} 的文本失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            output_log.info(f"获取 {img_desc} 元素 {loc} 的文本值为:{text}")
        return text

    def save_img(self, img_desc):
        """
        :param img_desc: 图片的描述 。格式为 页面名称_功能名
        :return:
        """
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 时间戳 time模块  不要有:
        img_name = "{}_{}.png".format(img_desc, now)
        img_path = os.path.join(SCREENSHOT_DIR, img_name)
        try:
            self.driver.save_screenshot(img_path)
        except:
            output_log.exception("网页截图失败！")
        else:
            output_log.info(f"截图成功，截图存放在：{img_path}")

    # toast获取
    def get_toast_msg(self, part_str):
        xpath = f'//*[contains(text(),"{part_str}")]'
        loc = By.XPATH, xpath
        try:
            self._deal_element(loc, part_str, 10, 0.01, wait_type='presence')
            text = self.get_text(loc, part_str)
        except:
            output_log.exception("获取toast信息失败！！")
            raise
        else:
            output_log.info(f'获取toast信息成功, --> {text}')
            return text

    # 获取当前页面源码
    def get_page_source(self):
        try:
            page_source = self.driver.page_source
        except:
            self.save_img("获取页面源码失败")
            output_log.exception("获取页面源码失败！")
            raise
        else:
            output_log.info("获取当前页面源码成功")
            return page_source
