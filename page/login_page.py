import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    name_edit_button = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_edit_button = By.ID, "com.tpshop.malls:id/edit_password"
    show_password_button = By.ID, "com.tpshop.malls:id/img_view_pwd"
    login_edit_button = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step(title="输入用户名")
    def input_name(self, text):
        allure.attach('用户名', text)
        self.input(self.name_edit_button, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        allure.attach('密码', text)
        self.input(self.password_edit_button, text)

    @allure.step(title="点击登录按钮")
    def click_login_button(self):
        self.click(self.login_edit_button)

    @allure.step(title="显示密码")
    def click_show_password(self):
        self.click(self.show_password_button)

    def is_login_button_enabled(self):
        return self.is_location_enabled(self.login_edit_button)
