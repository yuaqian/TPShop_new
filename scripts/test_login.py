import pytest


from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_with_file


class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_with_file("login_data", "test_login"))
    def test_login(self, args):
        name = args["name"]
        password = args["password"]
        expect = args["expect"]

        self.page.home_button.click_mine()
        self.page.mine_button.click_login()
        self.page.login_button.input_name(name)
        self.page.login_button.input_password(password)
        self.page.login_button.click_login_button()
        assert self.page.login_button.is_toast_exist(expect)
