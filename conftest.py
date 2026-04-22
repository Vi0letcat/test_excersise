import pytest
from selenium import webdriver
from pages.main_page import MainPage
from pages.reg_page import RegistrationPage
from pages.auth_page import AuthPage
from pages.download_page import DownloadPage
from api_requests import APIRequests
import random
import string

BASE_URL = "https://trueconf.ru/"


def pytest_addoption(parser):
    parser.addoption(
        "--addr",
        action="store",
        default="https://trueconf.ru/",
        help="base page address",
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--addr")


@pytest.fixture(scope="session")
def api_requests():
    return APIRequests()


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver, base_url):
    page = MainPage(driver, base_url)
    page.open()
    return page


@pytest.fixture()
def registration_page(driver, base_url):
    page = RegistrationPage(driver, base_url)
    page.open()
    return page


@pytest.fixture()
def auth_page(driver, base_url):
    page = AuthPage(driver, base_url)
    page.open()
    return page


@pytest.fixture()
def download_page(driver, base_url):
    page = DownloadPage(driver, base_url)
    page.open()
    return page


@pytest.fixture()
def random_string():
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(5))


@pytest.fixture(scope="class")
def random_string_cls():  # отдельная фикстура со скоупом на класс, чтобы тест авторизации проходил под тем же юзером что был созхдан в тесте регистрации
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(5))


@pytest.fixture()
def create_test_user(random_string, api_requests):
    user_data = api_requests.create_user(
        name=f"test_name_{random_string}",
        password=f"password_{random_string}",
        email=f"test_{random_string}@test.ru",
    )
    return (user_data, random_string)
