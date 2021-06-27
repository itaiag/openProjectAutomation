from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver

from infra.web.action_bot import ActionBot


class AbstractPage(ABC):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.bot = ActionBot(driver)
