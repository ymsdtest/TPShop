import time

from appium import webdriver

from common.base import Base

class OderPage(Base):
    """制作定位器"""
    my_loc = ("xpath","//*[@text='我的']")# 我的按钮
    remaining_loc = ("id","com.tpshop.malls:id/balance_tv")# 余额
    integral_loc = ("id","com.tpshop.malls:id/point_tv")# 积分
    homepage_loc = ("xpath","//*[@text='首页']")# 首页按钮
    goods_sale_loc = ("xpath","//*[@text='品牌街']")# 促销按钮
    # 选择商品
    mobile_loc = ("xpath","//*[@text='多规格衣服的的快递']")
    goods_money = ("id","com.tpshop.malls:id/balance_fee_tv")# 选择余额支付商品价格
    add_goods_loc = ("xpath","//*[@text='加入购物车']")# 加入购物车按钮
    ensure_loc = ("xpath","//*[@text='确定']")# 确定按钮
    click_goods_loc = ("xpath","//*[@text='购物车']")# 点击购物车
    now_buy_loc = ("xpath","//*[@text='立即购买']")# 立即购买按钮
    ensure2_loc = ("xpath", "//*[@text='确定']")  # 确定按钮
    money_loc = ("id","com.tpshop.malls:id/order_balance_sth") # 点击余额支付
    oder_pay_loc = ("xpath","//*[@text='提交订单']")# 提交订单按钮
    password_loc = ("id","com.tpshop.malls:id/pwd_et")# 密码输入框
    ensure1_loc = ("xpath", "//*[@text='确定']")# 确定按钮

    """封装表现层"""
    def click_my(self):
        """点击我的"""
        self.click(self.my_loc)
    def get_remaining(self):
        """获取余额文本"""

        res=self.get_element_text(self.remaining_loc)
        return res
    def get_integral(self):
        """获取积分文本"""
        res1 = self.get_element_text(self.integral_loc)
        return res1
    def clic_home(self):
        """点击首页"""
        self.click(self.homepage_loc)
    def click_goods_sale(self):
        """点击品牌街"""
        self.click(self.goods_sale_loc)
    def click_mobile(self):
        """选择商品"""
        self.click(self.mobile_loc)
    def text_goods_money(self):
        """获取余额"""
        return self.get_element_text(self.goods_money)
    def click_add_goods(self):
        """加入购物车"""
        self.click(self.add_goods_loc)
    def click_ensure(self):
        """点击确定添加"""
        self.click(self.ensure_loc)
    def click_good(self):
        """点击购物车"""
        self.click(self.click_goods_loc)
    def click_now_buy(self):
        """点击立即购买"""
        self.click(self.now_buy_loc)
    def click_money(self):
        """点击余额支付"""
        self.click(self.money_loc)
    def click_oder_pay(self):
        """点击提交订单"""
        self.click(self.oder_pay_loc)
    def input_password(self,password):
        """输入密码"""
        self.send_keys(self.password_loc,password)

    def click_ensure1(self):
        """点击确定"""
        self.click(self.ensure1_loc)
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
    oder = OderPage(driver)
    oder.click_my()
    time.sleep(5)
    remaining1 = oder.get_remaining()
    integral1 = oder.get_integral()
    oder.clic_home()
    time.sleep(3)
    oder.click_goods_sale()
    time.sleep(3)
    oder.click_mobile()
    time.sleep(3)
    oder.click_now_buy()
    time.sleep(3)
    oder.click_ensure()
    time.sleep(2)
    oder.click_money()
    time.sleep(3)
    oder.click_oder_pay()
    time.sleep(3)
    oder.input_password("123456")
    time.sleep(2)
    oder.click_ensure1()
    time.sleep(2)
    oder.back()
    time.sleep(2)
    oder.back()
    time.sleep(2)
    oder.back()
    time.sleep(2)
    oder.click_my()
    remaining2 = oder.get_remaining()
    integral2 = oder.get_integral()
    if remaining1 != remaining2 and integral1 != integral2:
        print("购买成功")
    else:
        print("购买失败")

