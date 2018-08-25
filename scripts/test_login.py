import random

import allure
import pytest
import time

from allure.constants import AttachmentType
from selenium.webdriver.common.by import By

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file


def random_password():
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password


def show_password_data():
    temp_list = list()
    for i in range(2):
        temp_list.append(random_password())
    return temp_list


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    # def test_login(self, args):
    #     name = args["name"]
    #     password = args["password"]
    #     expect = args["expect"]
    #
    #     self.page.home_button.click_mine()
    #     self.page.mine_button.click_login()
    #     self.page.login_button.input_name(name)
    #     self.page.login_button.input_password(password)
    #     self.page.login_button.click_login_button()
    #     assert self.page.login_button.is_toast_exist(expect)

    # @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login_miss_part"))
    # def test_login_miss_part(self, args):
    #     name = args["name"]
    #     password = args["password"]
    #
    #     self.page.home_button.click_mine()
    #     self.page.mine_button.click_login()
    #     self.page.login_button.input_name(name)
    #     self.page.login_button.input_password(password)
    #     assert not self.page.login_button.is_login_button_enabled()

    @pytest.mark.parametrize("password", show_password_data())
    def test_show_password(self, password):
        password_location = (By.XPATH, "//*[@text='%s']" % password)
        self.page.home_button.click_mine()
        self.page.mine_button.click_login()

        self.page.login_button.input_password(password)
        # 点击眼睛前，没有找到输入的密码
        assert not self.page.login_button.is_location_exist(password_location)
        self.page.login_button.click_show_password()
        time.sleep(2)
        allure.attach("显示密码：", self.driver.get_screenshot_as_png(), AttachmentType.PNG)
        assert self.page.login_button.is_location_exist(password_location)


