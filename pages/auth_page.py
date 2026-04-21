from pages.base_page import BasePage
from pages.base_page import BasePageLocators
from selenium.webdriver.common.by import By

class AuthPageLocators(BasePageLocators):
    id_input = (By.ID, "form-login")
    password_input = (By.ID, "form-password")
    submit_button = (By.CSS_SELECTOR, "button[type='submit']")

class AuthPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://trueconf.ru/login.html"
        self.locators = AuthPageLocators()
    
    def open(self):
        self.driver.get(self.url)
    
    def auth(self, id: str, password: str):
        self.fill_input(*self.locators.id_input, value=id)
        self.fill_input(*self.locators.password_input, value=password)
        self.click_button(*self.locators.submit_button)