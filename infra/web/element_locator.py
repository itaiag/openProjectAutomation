from selenium.webdriver.common.by import By


class ElementLocator:

    def __init__(self, by: By, value: str, description: str = ""):
        self.by = by
        self.value = value
        self.description = description
