import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from infra.pages.abstract_page import AbstractPage

from infra.web.element_locator import ElementLocator


class NewWorkPackagePage(AbstractPage):

    subject_input = ElementLocator(By.ID, "wp-new-inline-edit--field-subject", "'Subject' input")
    description_text_box = ElementLocator(By.XPATH, "//div[@role='textbox']", "'Description' text box")
    save_button = ElementLocator(By.ID, "work-packages--edit-actions-save", "'Save' button")
    workpackage_type_button = ElementLocator(By.CSS_SELECTOR, "div.type [role='button']", "'Work package type' button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def write_subject(self, subject):
        self.bot.send_keys(self.subject_input, subject)
        return self

    def write_description(self, description):
        self.bot.send_keys(self.description_text_box, description)
        return self

    def click_save_button(self):
        self.bot.click(self.save_button)
        from infra.pages.work_packages_page import WorkPackagesPage
        time.sleep(2)
        return WorkPackagesPage(self.driver)

    def get_work_package_type_button_text(self) -> str:
        type_text = self.bot.get_text(self.workpackage_type_button)
        return type_text
