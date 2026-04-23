import pytest
from selenium.webdriver.common.by import By


class TestTrueConf:
    def test_open_page(self, main_page):
        main_page.wait_until_element_is_visible(
            *main_page.locators.header_menu
        )  # проверяем что появилась менюшка. для smoke вполне достаточно как факт открытия страницы.

    @pytest.mark.dependency(name="registration")
    def test_registration(self, registration_page, random_string_cls):
        registration_page.open()
        registration_page.registration(
            id=f"test_user_{random_string_cls}",
            email=f"test_{random_string_cls}@test.ru",
            password=f"password_{random_string_cls}",
            full_name=f"Test Name {random_string_cls}",
        )
        registration_page.wait_until_element_is_visible(
            *registration_page.locators.header_username
        )
        registration_page.check_element_text_equals(
            *registration_page.locators.header_username,
            expected_text=f"Test Name {random_string_cls}",
        )

    # Использован моуль pytest-dependency, чтобы тест пропускался если юзер не создан.
    # Либо можно создать тестового юзера фикстурой, например инсёром в БД, но у меня такого доступа нет.
    @pytest.mark.dependency(name="auth", depends=["registration"])
    def test_auth(self, auth_page, random_string_cls):
        auth_page.auth(
            id=f"test_user_{random_string_cls}",
            password=f"password_{random_string_cls}",
        )
        auth_page.wait_until_element_is_visible(*auth_page.locators.header_username)
        auth_page.check_element_text_equals(
            *auth_page.locators.header_username,
            expected_text=f"Test Name {random_string_cls}",
        )

    @pytest.mark.parametrize(
        "title, expected_url, expected_text",
        [
            ("Windows", "windows", "Windows"),
            ("macOS", "mac", "macOS"),
            ("Linux", "linux", "Linux"),
            (
                "iOS",
                "ios",
                "Видеозвонки и конференции",
            ),  # На странице iOS нет упоминания iOS в заголовке. Возможно это не лучший вариант для проверки.
            ("Android", "android", "Android"),
            ("Аврора", "avrora", "Аврора"),
            ("Android TV", "android-tv", "Android TV"),
            ("Браузеры", "web-client", "браузера"),
        ],
    )
    def test_download_options(self, download_page, title, expected_url, expected_text):
        download_page.wait_and_find_element(
            By.XPATH, f"//a/span[text()='{title}']"
        ).click()  # Ищем элемент с заголовкам ОС/среды. Ошибка если не находим, кликаем если находим.
        download_page.check_url_contains(expected_url)  # Проверяем урл
        download_page.check_element_text_contains(
            *download_page.locators.version_page_header, expected_text=expected_text
        )  # Проверяем что текст на странице соответсвует выбранному варианту

    def test_access_download_page_from_main(self, main_page):
        """
        ТЗ гласило "С главной страницы, переходя на скачивание, убедиться в наличии 7 вариантов установки
        В моём понимании тесты должны работать отдельно друг от друга, и если это тест проверки контента, то проверять переход туда в нём же не нужно
        Но на всякий случай вот тест перехода на старницу загрузок с главной
        """
        main_page.wait_until_element_is_visible(
            *main_page.locators.download_button_popup
        ).click()
        main_page.wait_until_element_is_visible(
            *main_page.locators.download_button_desktop
        ).click()
        main_page.check_url_contains("downloads")
