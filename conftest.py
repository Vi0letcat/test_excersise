import pytest
from selenium import webdriver
from pages.reg_page import RegistrationPage
from pages.auth_page import AuthPage
from pages.download_page import DownloadPage
from requests import Requests
import random
import string

BASE_URL = "https://trueconf.ru/" 

@pytest.fixture()
def api_requests():
    return Requests()

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--addr")

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

@pytest.fixture()
def download_page(driver, base_url):
    return DownloadPage(driver, base_url)

@pytest.fixture()
def random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(5))

@pytest.fixture()
def create_test_user(random_string, api_requests):
    user_data = api_requests.create_user(
        name=f"test_name_{random_string}",
        password=f"password_{random_string}",
        email=f"test_{random_string}@test.ru"
    )
    return (user_data, random_string)