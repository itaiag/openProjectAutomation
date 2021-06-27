from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from infra.pages.home_page import HomePage
from infra.pages.login_page import LoginPage
from infra.web.browser_type import BrowserType
from infra.web.web_driver_factory import WebDriverFactory
from main_config import config

driver: WebDriver = None


def browse_to_url(url: str):
    global driver
    if driver is None:
        driver = WebDriverFactory.create_web_driver(BrowserType.CHROME)
    driver.get(url)


def do_ui_login(username: str, password: str) -> HomePage:
    browse_to_url(config["base_url"])
    login_page = LoginPage(driver)
    login_page\
        .write_username(username)\
        .write_password(password)

    home_page = login_page.click_sign_in_button()
    return home_page
