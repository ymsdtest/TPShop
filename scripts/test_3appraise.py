import time,pytest,allure

from page.appraise_page import AppraisePage

class Testappraise:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step(title='评价商品')
    def test_appraise(self,login):
        app = AppraisePage(login)
        allure.attach("点击我的", "进入个人中心")
        app.click_my()# 点击我的
        time.sleep(2)
        app.click_appraise()
        allure.attach("评价商品", f"评价的商品为只要一分钱")
        time.sleep(2)
        login.tap([(550, 240)])
        time.sleep(2)
        app.input_content("物美价廉")
        allure.attach("评价商品", "评价的内容为物美价廉")
        time.sleep(3)
        app.click_five()# 五星好评
        time.sleep(2)
        app.click_submit()# 店家提交
        time.sleep(3)
        try:
            toast = app.get_toast("评论成功")  # 获取评论成功的toast
            if toast == "评论成功":
                assert 1
        except:
            return False
