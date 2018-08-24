from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    name_edit_button = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_edit_button = By.ID, "com.tpshop.malls:id/edit_password"
    login_edit_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_name(self, text):
        self.input(self.name_edit_button, text)

    def input_password(self, text):
        self.input(self.password_edit_button, text)

    def click_login_button(self):
        self.click(self.login_edit_button)
