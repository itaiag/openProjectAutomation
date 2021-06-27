from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from infra.pages.abstract_page import AbstractPage
from infra.pages.new_work_package_page import NewWorkPackagePage
from infra.web.element_locator import ElementLocator


class WorkPackagesPage(AbstractPage):

    projects_menu_button = ElementLocator(By.ID, "projects-menu", "'Projects Menu' button")
    create_button = ElementLocator(By.CSS_SELECTOR, "button[aria-label='Create new work package']", "'+ Create' button")
    task_menu_item = ElementLocator(By.CSS_SELECTOR, "a[aria-label='Task']", "'Task' menu item")
    milestone_menu_item = ElementLocator(By.CSS_SELECTOR, "a[aria-label='Milestone']", "'Milestone' menu item")
    phase_menu_item = ElementLocator(By.CSS_SELECTOR, "a[aria-label='Phase']", "'Phase' menu item")
    workpackage_table_rows = ElementLocator(By.CSS_SELECTOR, "tr.wp--row", "'Work package' table rows")
    cell_id = ElementLocator(By.CSS_SELECTOR, "td.id", "'ID' table cell")
    cell_subject = ElementLocator(By.CSS_SELECTOR, "td.subject", "'Subject' table cell")
    cell_type = ElementLocator(By.CSS_SELECTOR, "td.type", "'Type' table cell")
    cell_status = ElementLocator(By.CSS_SELECTOR, "td.status", "'Status' table cell")
    cell_assignee = ElementLocator(By.CSS_SELECTOR, "td.assignee", "'Assignee' table cell")
    cell_priority = ElementLocator(By.CSS_SELECTOR, "td.priority", "'Priority' table cell")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_project_menu_title(self) -> str:
        menu_title = self.bot.get_text(self.projects_menu_button)
        return menu_title

    def select_create_task(self) -> NewWorkPackagePage:
        self.bot.click(self.create_button)
        self.bot.click(self.task_menu_item)
        return NewWorkPackagePage(self.driver)

    def get_number_of_table_rows(self):
        row_elements = self.bot.get_elements(self.workpackage_table_rows)
        return len(row_elements)

    def read_table_row(self, row_index):
        row_elements = self.bot.get_elements(self.workpackage_table_rows)
        row_element = row_elements[row_index]

        row_dict = {
            "id": self.bot.get_inner_element_text(row_element, self.cell_id),
            "subject": self.bot.get_inner_element_text(row_element, self.cell_subject),
            "type": self.bot.get_inner_element_text(row_element, self.cell_type),
            "status": self.bot.get_inner_element_text(row_element, self.cell_status),
            "assignee": self.bot.get_inner_element_text(row_element, self.cell_assignee),
            "priority": self.bot.get_inner_element_text(row_element, self.cell_priority)
        }

        return row_dict
