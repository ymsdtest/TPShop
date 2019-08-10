
from appium import webdriver


import pytest

@pytest.fixture()
def login():
    desired_caps = {"platformName": "android",
                    "platformVersion": "5.1.1",
                    "deviceName": "127.0.0.1:21503",
                    "appPackage": "com.tpshop.malls",
                    "appActivity": ".SPMainActivity",
                    "unicodeKeyboard": True,
                    "resetKeyboard": True,
                    "noReset": True,
                    "automationName": "Uiautomator2"
                    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    return driver



