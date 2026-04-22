import pytest
from time import sleep
from selenium.webdriver.common.by import By


TEST_PASSWORD = "!QAZ2wsx"

class TestTrueConf:
    def test_open_page(base_page):
        base_page.open()
        assert "TrueConf" in base_page.driver.title

    def test_registration(registration_page, random_user_id, random_email, random_name):
        registration_page.open()
        registration_page.registration(id = random_user_id, email = random_email, password = TEST_PASSWORD, name = random_name)
        registration_page.check_element_text_equals(*registration_page.locators.header_username, expected_text=random_name)

    def test_auth(auth_page, random_user_id, random_password, random_name):
        auth_page.open()
        auth_page.auth(random_user_id, random_password)
        auth_page.wait_until_element_is_visible(*auth_page.locators.header_username)
        auth_page.check_element_text_equals(*auth_page.locators.header_username, expected_text=random_name)

    @pytest.mark.parametrize("title, expected_url", [
        ("Windows", "windows"),
        ("macOS", "mac"),
        ("Linux", "linux"),
        ("iOS", "ios"),
        ("Android", "android"),
        ("Аврора", "avrora"),
        ("Android TV", "android-tv"),
    ])
    def test_download_options(download_page, title, expected_url):
        download_page.open()
        download_page.find_element(By.XPATH, f"//a/span[text()='{title}']").click()
        download_page.check_url_contains(expected_url)
        # download_page.wait_until_element_is_visible(*download_page.locators.download_button)
        