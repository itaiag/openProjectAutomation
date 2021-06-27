from infra.web.browser_type import BrowserType
from selenium import webdriver


class WebDriverFactory:

    @staticmethod
    def create_web_driver(browser_type: BrowserType):

        driver = None

        if browser_type == BrowserType.CHROME:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=chrome_options)

        elif browser_type == BrowserType.FIREFOX:
            driver = webdriver.Firefox()

        return driver
