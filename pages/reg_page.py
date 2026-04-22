from pages.base_page import BasePage
from pages.base_page import BasePageLocators
from selenium.webdriver.common.by import By


class RegistrationPageLocators(BasePageLocators):
    id_input = (By.ID, "person-reg-login")
    email_input = (By.ID, "person-reg-email")
    password_input = (By.ID, "person-reg-password")
    full_name_input = (By.ID, "person-reg-full_name")
    privacy_policy_checkbox = (By.ID, "person-reg-privacy_policy")
    agreement_checkbox = (By.ID, "person-reg-personal_data_processing_consent_checkbox")
    submit_button = (By.CSS_SELECTOR, ".registration .waves-button-input")


class RegistrationPage(BasePage):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = f"{base_url}products/online/registration-standard.html"
        self.locators = RegistrationPageLocators()

    def open(self):
        self.driver.get(self.url)

    def registration(self, id: str, email: str, password: str, full_name: str):
        self.fill_input(*self.locators.id_input, value=id)
        self.fill_input(*self.locators.email_input, value=email)
        self.fill_input(*self.locators.password_input, value=password)
        self.fill_input(*self.locators.full_name_input, value=full_name)
        self.select_checkbox(*self.locators.privacy_policy_checkbox)
        self.select_checkbox(*self.locators.agreement_checkbox)
        self.js_click(self.find_element(*self.locators.submit_button))
