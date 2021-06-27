from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from infra.pages.abstract_page import AbstractPage
from infra.pages.new_project_page import NewProjectPage
from infra.pages.project_overview_page import ProjectOverviewPage
from infra.web.element_locator import ElementLocator


class HomePage(AbstractPage):

    new_project_button = ElementLocator(By.CSS_SELECTOR, "div.projects a[title='New project']", "'New Project' button")
    select_project_button = ElementLocator(By.ID, "projects-menu", "'Select a project' button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_new_project_button(self) -> NewProjectPage:
        self.bot.click(self.new_project_button)
        return NewProjectPage(self.driver)

    def select_project(self, project_name) -> ProjectOverviewPage:
        self.bot.click(self.select_project_button)
        self.bot.click(ElementLocator(By.XPATH, f"//li//a[text()='{project_name}']", f"'{project_name}' link"))
        return ProjectOverviewPage(self.driver)
