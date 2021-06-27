import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from infra.pages.abstract_page import AbstractPage
from infra.pages.work_packages_page import WorkPackagesPage
from infra.web.element_locator import ElementLocator


class NewProjectPage(AbstractPage):

    project_name_input = ElementLocator(By.ID, "project_name", "'Project Name' input")
    advanced_settings_title = ElementLocator(By.XPATH, "//a[text()='Advanced settings']", "'Advanced settings' title")
    project_description_text_box = ElementLocator(By.XPATH, "//textarea[@id='project_description']/..//div[@role='textbox']", "'Project Description' text box")
    project_identifier_input = ElementLocator(By.ID, "project_identifier", "'Project Identifier' input")
    status_select = ElementLocator(By.ID, "project_status_code", "'Status' select")
    create_button = ElementLocator(By.CSS_SELECTOR, "button[type='submit']", "'Create' button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def write_project_name(self, project_name: str):
        self.bot.send_keys(self.project_name_input, project_name)
        return self

    def click_advanced_settings_title(self):
        self.bot.click(self.advanced_settings_title)
        return self

    def write_description(self, description: str):
        self.bot.click(self.project_description_text_box)
        self.bot.send_keys(self.project_description_text_box, description)
        return self

    def get_project_identifier(self) -> str:
        project_identifier = self.bot.get_attribute_value(self.project_identifier_input, "value")
        return project_identifier

    def select_status(self, status: str):
        self.bot.select_by_visible_text(self.status_select, status)
        return self

    def click_create_button(self) -> WorkPackagesPage:
        self.bot.click(self.create_button)
        return WorkPackagesPage(self.driver)
