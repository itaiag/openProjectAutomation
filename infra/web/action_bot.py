from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from infra.web.element_locator import ElementLocator


class ActionBot:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, element_locator: ElementLocator):
        element = self.get_element(element_locator)
        element.click()

    def send_keys(self, element_locator: ElementLocator, text: str):
        element = self.get_element(element_locator)
        element.clear()
        element.send_keys(text)

    def get_attribute_value(self, element_locator: ElementLocator, attribute_name: str) -> str:
        element = self.get_element(element_locator)
        attribute_value = element.get_attribute(attribute_name)
        return attribute_value

    def select_by_visible_text(self, element_locator: ElementLocator, visible_text: str):
        select_element = self.get_element(element_locator)
        select = Select(select_element)
        select.select_by_visible_text(visible_text)

    def select_by_value(self, element_locator: ElementLocator, value: str):
        select_element = self.get_element(element_locator)
        select = Select(select_element)
        select.select_by_value(value)

    def get_text(self, element_locator: ElementLocator) -> str:
        element = self.get_element(element_locator, element_must_be_visible=False)
        text = element.text
        return text

    def get_inner_element_text(self, outer_element: WebElement, inner_element_locator: ElementLocator) -> str:
        element = self.get_inner_element(outer_element, inner_element_locator)
        text = element.text
        return text

    def get_element(self, element_locator: ElementLocator, timeout_in_seconds: int = 5, element_must_be_visible: bool = True) -> WebElement:
        if element_must_be_visible:
            return self.wait_for_visibility_of_element(element_locator, timeout_in_seconds)
        else:
            return self.wait_for_presence_of_element(element_locator, timeout_in_seconds)

    def get_elements(self, element_locator: ElementLocator) -> [WebElement]:
        elements = self.driver.find_elements(element_locator.by, element_locator.value)
        return elements

    def get_inner_element(self, outer_element: WebElement, inner_element_locator: ElementLocator) -> WebElement:
        inner_element = outer_element.find_element(inner_element_locator.by, inner_element_locator.value)
        return inner_element

    def wait_for_presence_of_element(self, element_locator: ElementLocator, timeout_in_seconds: int = 5) -> WebElement:
        element = WebDriverWait(self.driver, timeout_in_seconds).until(expected_conditions.presence_of_element_located((element_locator.by, element_locator.value)))
        return element

    def wait_for_visibility_of_element(self, element_locator: ElementLocator, timeout_in_seconds: int = 5) -> WebElement:
        element = WebDriverWait(self.driver, timeout_in_seconds).until(expected_conditions.visibility_of_element_located((element_locator.by, element_locator.value)))
        return element


