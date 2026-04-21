import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.reg_page import RegistrationPage
from pages.auth_page import AuthPage
from pages.download_page import DownloadPage
import random
import string

BASE_URL = "https://trueconf.ru/" 

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def registration_page(driver, base_url):
    return RegistrationPage(driver, base_url)

@pytest.fixture()
def auth_page(driver, base_url):
    return AuthPage(driver, base_url)

@pytest.fixture(scope="session", autouse=True)
def random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(5))

@pytest.fixture()
def download_page(driver, base_url):
    return DownloadPage(driver, base_url)

@pytest.fixture(scope="session")
def random_user_id(random_string):
    return f"test_user_{random_string}"

@pytest.fixture(scope="session")
def random_email(random_user_id):
    return f"{random_user_id}@example.com"

@pytest.fixture(scope="session")
def random_name(random_user_id, random_string):
    return f"Test User {random_string}"