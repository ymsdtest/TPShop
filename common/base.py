import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.size = self.driver.get_window_size()
    def find_element(self,locator,timeout=10):
        """
        定位一个元素,返回一个列表
        :param locator:
        :param timeout:
        :return:
        """
        try:
            element = WebDriverWait(self.driver,timeout,0.5).until(EC.presence_of_element_located(locator))
        except:
            return False
        else:
            return element
    def find_elements(self,locator,timeout=10):
        """
        定位一组元素返回元素列表
        :param locator:
        :param timeout:
        :return:
        """
        elements = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        return elements
    def click(self,locator,timeout=10):
        """
        点击元素
        :param locator:
        :param timeout:
        :return:
        """
        try:
            element = self.find_element(locator=locator,timeout=timeout)
            element.click()
        except:
            return False
    def send_keys(self,locator,text,timeout=10):
        """
        输入
        :param locator:
        :param timeout:
        :return:
        """

        element = self.find_element(locator=locator,timeout=timeout)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """获取元素的文本(text)"""
        text = self.find_element(locator).get_attribute("text")
        return text

    def back(self):
        """后退"""
        self.driver.back()
    def swipe_up(self):
        """向上滑动"""
        x1 = self.size["width"]*0.5 # x坐标
        y1 = self.size['height']*0.75 #启动点
        y2 = self.size['height']*0.25 # 终点
        self.driver.swipe(x1,y1,x1,y2,5000)
    def swipe_down(self):
        """向下移动"""
        x1 = self.size["width"] * 0.5  # x坐标
        y1 = self.size['height'] * 0.25  # 启动点
        y2 = self.size['height'] * 0.75 #5  终点
        self.driver.swipe(x1, y1, x1, y2,5000)

    def swipe_left(self):
        """向左移动"""
        size = self.driver.get_window_size()
        y1 = size["height"]*0.5  # y坐标
        x1 = size['width']*0.95  # 起点
        x2 = size['width']*0.15  # 终点
        self.driver.swipe(y1,x1,y1,x2,3000)
    def swipe_right(self):
        """向右移动"""
        size = self.driver.get_window_size()
        y1 = size["height"] * 0.5  # y坐标
        x1 = size['width'] * 0.15  # 起点
        x2 = size['width'] * 0.95  # 终点
        self.driver.swipe(y1, x1, y1, x2, 3000)

    def focus_element(self,locator):
        """聚焦元素"""
        while True:
            try:
                self.click(locator=locator)
                break
            except:
                self.swipe_up()
                time.sleep(1)
    def get_toast(self,text: str):
        """
        获取toast文本内容
        :param text:
        :return:
        """
        try:
            message_loc = ("xpath",f"//*[contains(@text,'{text}')]")
            element = WebDriverWait(self.driver,10,0.1).until(EC.presence_of_element_located(message_loc))
            message = element.get_attribute("text")
            return message
        except TimeoutError:
            print("没有toast标签")
