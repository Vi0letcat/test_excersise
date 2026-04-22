import pytest
from selenium.webdriver.common.by import By
from time import sleep


class TestTrueConf:
    def test_open_page(self, main_page):
        main_page.wait_until_element_is_visible(*main_page.locators.header_menu)

    @pytest.mark.dependency(name='registration')
    def test_registration(self, registration_page, random_string_cls):
        registration_page.open()
        registration_page.registration(
            id = f"test_user_{random_string_cls}",
            email = f"test_{random_string_cls}@test.ru",
            password = f"password_{random_string_cls}",
            full_name = f"Test Name {random_string_cls}"
        )
        registration_page.wait_until_element_is_visible(*registration_page.locators.header_username)
        registration_page.check_element_text_equals(*registration_page.locators.header_username, expected_text=f"Test Name {random_string_cls}")

    @pytest.mark.dependency(name='auth', depends=['registration'])
    def test_auth(self, auth_page, random_string_cls):
        auth_page.auth(id = f"test_user_{random_string_cls}", password = f"password_{random_string_cls}")
        auth_page.wait_until_element_is_visible(*auth_page.locators.header_username)
        auth_page.check_element_text_equals(*auth_page.locators.header_username, expected_text=f"Test Name {random_string_cls}")

    @pytest.mark.parametrize("title, expected_url, expected_text", [
        ("Windows", "windows",  "Windows"),
        ("macOS", "mac", "macOS"),
        ("Linux", "linux", "Linux"),
        ("iOS", "ios", "Видеозвонки и конференции"),
        ("Android", "android", "Android"),
        ("Аврора", "avrora", "Аврора"),
        ("Android TV", "android-tv", "Android TV"),
        ("Браузеры", "web-client", "браузера")
    ])
    def test_download_options(self, download_page, title, expected_url, expected_text):
        download_page.open()
        download_page.find_element(By.XPATH, f"//a/span[text()='{title}']").click()
        download_page.check_url_contains(expected_url)
        download_page.check_element_text_contains(*download_page.locators.version_page_header, expected_text=expected_text)