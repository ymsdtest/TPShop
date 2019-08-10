from common.base import Base
class OderOtherPage(Base):
    """制作定位器"""
    my_loc = ("xpath", "//*[@text='我的']")  # 我的按钮
    remaining_loc = ("id", "com.tpshop.malls:id/balance_tv")  # 余额
    integral_loc = ("id", "com.tpshop.malls:id/point_tv")  # 积分
    homepage_loc = ("xpath", "//*[@text='首页']")  # 首页按钮
    goods_loc = ("xpath","//*[@text='航测试手机']")#选择商品
    now_buy_loc = ("xpath", "//*[@text='立即购买']")  # 立即购买按钮
    goods_money = ("id","com.tpshop.malls:id/balance_fee_tv")# 选择余额支付商品价格

    money_loc = ("id", "com.tpshop.malls:id/order_balance_sth")  # 点击余额支付
    oder_pay_loc = ("xpath", "//*[@text='提交订单']")  # 提交订单按钮
    password_loc = ("id", "com.tpshop.malls:id/pwd_et")  # 密码输入框
    ensure1_loc = ("xpath", "//*[@text='确定']")  # 确定按钮
    """封装操作层"""
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
    def click_goods(self):
        """选择商品"""
        self.swipe_up()
        self.click(self.goods_loc)

    def click_now_buy(self):
        """点击立即购买"""
        self.click(self.now_buy_loc)

    def click_money(self):
        """点击余额支付"""
        self.click(self.money_loc)
    def text_goods_money(self):
        """获取余额"""
        return self.get_element_text(self.goods_money)
    def click_oder_pay(self):
        """点击提交订单"""
        self.click(self.oder_pay_loc)
    def input_password(self,password):
        """输入密码"""
        self.send_keys(self.password_loc,password)

    def click_ensure1(self):
        """点击确定"""
        self.click(self.ensure1_loc)