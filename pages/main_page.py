from pages.base_page import BasePage
from pages.base_page import BasePageLocators

class MainPageLocators(BasePageLocators):
    pass

class MainPage(BasePage):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.locators = MainPageLocators()