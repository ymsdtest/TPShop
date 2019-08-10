import time
from common.base import Base
from appium import webdriver
class AppraisePage(Base):
    """制作定位器"""
    my_loc = ("xpath", "//*[@text='我的']")  # 我的按钮
    appraise_loc = ("xpath","//*[@text='待评价']")# 待评价
    content_loc = ("xpath","//*[@text='请输入评价']")# 评价输入框
    five_loc = ("id","com.tpshop.malls:id/star5_btn") # 五星好评
    submit_loc = ("xpath", "//*[@text='提交']")# 提交按钮
    """操作"""
    def click_my(self):
        """点击我的"""
        self.click(self.my_loc)
    def click_appraise(self):
        """点击待评价"""
        self.click(self.appraise_loc)
    def input_content(self,text):
        """输入评价内容"""
        self.send_keys(self.content_loc,text)
    def click_five(self):
        """五星好评"""
        elements = self.find_elements(self.five_loc)
        for element in elements:
            element.click()
    def click_submit(self):
        """点击提交"""
        self.click(self.submit_loc)
if __name__ == '__main__':
    desired_caps = {"platformName": "android",
                    "platformVersion": "5.1.1",
                    "deviceName": "127.0.0.1:21503",
                    "appPackage": "com.tpshop.malls",
                    "appActivity": ".SPMainActivity",
                    "unicodeKeyboard": True,
                    "resetKeyboard": True,
                    "noReset": True,

                    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    app = AppraisePage(driver)
    app.click_my()
    time.sleep(2)
    app.click_appraise()
    time.sleep(2)
    driver.tap([(550,240)])
    time.sleep(2)
    app.input_content("物美价廉")
    time.sleep(3)
    app.click_five()
    time.sleep(2)
    app.click_submit()