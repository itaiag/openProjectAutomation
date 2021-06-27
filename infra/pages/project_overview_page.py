import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from infra.pages.abstract_page import AbstractPage
from infra.pages.work_packages_page import WorkPackagesPage
from infra.web.element_locator import ElementLocator


class ProjectOverviewPage(AbstractPage):

    work_packages_menu_link = ElementLocator(By.ID, "main-menu-work-packages", "'Work packages' menu link")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_work_packages_link(self) -> WorkPackagesPage:
        self.bot.click(self.work_packages_menu_link)
        time.sleep(2)
        return WorkPackagesPage(self.driver)
