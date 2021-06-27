from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from infra.pages.abstract_page import AbstractPage
from infra.pages.home_page import HomePage
from infra.web.element_locator import ElementLocator


class LoginPage(AbstractPage):

    username_input = ElementLocator(By.ID, "username", "'Username' input")
    password_input = ElementLocator(By.ID, "password", "'Password' input")
    sign_in_button = ElementLocator(By.CSS_SELECTOR, "#login-form [name='login']", "'Sign in' button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def write_username(self, username: str):
        self.bot.send_keys(self.username_input, username)
        return self

    def write_password(self, password: str):
        self.bot.send_keys(self.password_input, password)
        return self

    def click_sign_in_button(self) -> HomePage:
        self.bot.click(self.sign_in_button)
        return HomePage(self.driver)
