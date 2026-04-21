from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageLocators:
    header_username = (By.CSS_SELECTOR, ".header-menu__btn-text--user-name")

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://trueconf.ru/"
        self.locators = BasePageLocators()

    def open(self):
        self.driver.get(self.base_url)

    def find_element(self, *locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def wait_until_element_is_visible(self, *locator, timeout=10):
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator), message=f"Element with locator {locator} is not visible after {timeout} seconds")

    def check_url_contains(self, expected_substring: str, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_substring), message=f"URL does not contain '{expected_substring}' after {timeout} seconds")

    def fill_input(self, *locator, value: str):
        input_element = self.find_element(*locator)
        input_element.clear()
        input_element.send_keys(value)
    
    def select_checkbox(self, *locator):
        checkbox = self.find_element(*locator)
        if not checkbox.is_selected():
            checkbox.click()

    def click_button(self, *locator):
        button = self.find_element(*locator)
        button.click()

    def check_element_text_equals(self, *locator, expected_text: str):
        element = self.find_element(*locator)
        assert element.text == expected_text, f"Expected text '{expected_text}' but got '{element.text}'"
