from pages.base_page import BasePage
from pages.base_page import BasePageLocators
from selenium.webdriver.common.by import By

class DownloadPageLocators(BasePageLocators):
    pass

class DownloadPage(BasePage):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}downloads/"
        self.locators = DownloadPageLocators()
    
    def open(self):
        self.driver.get(self.url)