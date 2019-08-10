import time,pytest,allure

from page.oder_other_page import OderOtherPage

class TestOderOuther:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step(title='使用余额购物')
    def test_oder_outher(self,login):
        oder = OderOtherPage(login)
        allure.attach("点击我的", "进入个人中心")
        oder.click_my()# 点击我的
        time.sleep(5)
        remaining1 = oder.get_remaining()# 获取购买前的余额
        allure.attach("获取购物前的余额", f"购物前的余额为{remaining1}")
        allure.attach("点击首页", "进入首页")
        oder.clic_home()# 点击首页
        time.sleep(3)
        oder.click_goods()# 选择商品
        allure.attach("选择商品", "选择的商品为航测试手机")
        oder.click_now_buy()# 点击立即购买
        time.sleep(2)
        oder.click_ensure1()# 点击确认购买

        time.sleep(2)
        oder.click_money()# 选择余额支付
        money = oder.text_goods_money()  # 获取选择余额支付后商品的价格
        allure.attach("获取余额支付金额", f"金额为{money}")
        oder.click_oder_pay()# 点击提交订单
        time.sleep(3)
        oder.input_password("123456")# 输入密码
        time.sleep(2)
        oder.click_ensure1()# 点击确定
        time.sleep(2)
        oder.back()
        time.sleep(2)
        oder.back()
        time.sleep(2)
        oder.back()
        time.sleep(2)
        oder.click_my()
        remaining2 = oder.get_remaining()# 获取购物后的余额

        """购买前的金额-购买后的金额=选择余额支付后商品的价格"""
        assert float(remaining1) - float(remaining2) == float(money.strip('¥'))
        login.quit()