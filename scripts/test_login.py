from base.base_driver import init_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_login1(self):
        self.page.home_button.click_mine()
        self.page.mine_button.click_login()
        self.page.login_button.input_name("13800138006")
        self.page.login_button.input_password("123456")
        self.page.login_button.click_login_button()
