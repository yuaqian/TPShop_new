from page.home_page import HomePage
from page.mine_page import MinePage
from page.login_page import LoginPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home_button(self):
        return HomePage(self.driver)

    @property
    def mine_button(self):
        return MinePage(self.driver)

    @property
    def login_button(self):
        return LoginPage(self.driver)
