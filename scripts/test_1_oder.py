import time,pytest,allure

from page.oder_page import OderPage

class TestOder:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step(title='使用余额购物')
    def test_oder(self,login):
        """购买流程"""
        oder = OderPage(login)
        allure.attach("点击我的", "进入个人中心")
        oder.click_my()# 点击我的

        remaining1 = oder.get_remaining()# 获取购买前的余额
        allure.attach("获取购物前的余额", f"购物前的余额为{remaining1}")
        allure.attach("点击首页", "进入首页")
        oder.clic_home()# 点击首页
        goods=oder.click_goods_sale()
        allure.attach("选择商品", f"选择的商品为{goods}")
        time.sleep(3)
        login.tap([(250,250)])# 选择商品


        oder.click_now_buy()# 点击立即购买

        oder.click_ensure()# 点击确认购买
        time.sleep(2)
        oder.click_money()# 选择余额支付
        time.sleep(2)
        money = oder.text_goods_money()# 获取选择余额支付后商品的价格
        allure.attach("获取余额支付金额", f"金额为{money}")
        oder.click_oder_pay()# 提交订单

        oder.input_password("123456")# 输入支付密码

        oder.click_ensure1()# 点击确定

        time.sleep(2)
        oder.back()
        time.sleep(2)
        oder.back()
        time.sleep(2)
        oder.back()
        time.sleep(2)
        oder.click_my()# 点击我的

        remaining2 = oder.get_remaining()# 获取购物后的余额
        allure.attach("获取购物后的余额", f"购物前后余额为{remaining2}")
        login.quit()

        """购买前的金额-购买后的金额=选择余额支付后商品的价格"""
        assert float(remaining1)-float(remaining2)==float(money.strip('¥'))
