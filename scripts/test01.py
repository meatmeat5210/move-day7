import os
import sys

import pytest

sys.path.append(os.getcwd())
import allure

class Test01:
    def test0(self):
        allure.attach("点击新增地址按钮", "")
        allure.attach("点击新增输入收件人：", "")
        allure.attach("点击新增输入手机号：", "")
        allure.attach("点击新增输入收货地址：", "")
        allure.attach("点击新增输入点击新增：", "")
        print("test001被执行")

        allure.attach("点击新增输入点击更新：", "")

    # @allure.step("更新地址方法被执行")
    def test002(self):
        print("test002被执行")
    #官网推荐
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test003(self):
        print("断言失败,截图并写入报告")
        with open("./image/faile.png","rb")as f:
            allure.attach("失败原因:",f.read(),allure.attach_type.PNG)
            assert False

    def test004(self):
        print("test004被执行")