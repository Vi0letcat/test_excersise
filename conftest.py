import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.reg_page import RegistrationPage
from pages.auth_page import AuthPage
from pages.download_page import DownloadPage
import random
import string

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def base_page(driver):
    return BasePage(driver)

@pytest.fixture()
def registration_page(driver):
    return RegistrationPage(driver)

@pytest.fixture()
def auth_page(driver):
    return AuthPage(driver)

@pytest.fixture(scope="session", autouse=True)
def random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(5))

@pytest.fixture()
def download_page(driver):
    return DownloadPage(driver)

@pytest.fixture(scope="session")
def random_user_id(random_string):
    return f"test_user_{random_string}"

@pytest.fixture(scope="session")
def random_email(random_user_id):
    return f"{random_user_id}@example.com"

@pytest.fixture(scope="session")
def random_name(random_user_id, random_string):
    return f"Test User {random_string}"