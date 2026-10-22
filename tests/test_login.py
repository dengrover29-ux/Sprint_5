import pytest

from page_objects import MainPage, LoginPage, ProfilePage, RegisterPage, RecoveryPage
from test_data import TEST_USER


@pytest.mark.login
class TestLogin:
    def test_login_via_main_page(self, driver, wait):
        # Вход по кнопке «Войти в аккаунт» на главной
        main = MainPage(driver, wait)
        main.open_main()
        main.click_login_header()
        LoginPage(driver, wait).login(TEST_USER["email"], TEST_USER["password"])
        profile = ProfilePage(driver, wait)
        assert profile.is_logged_in()

    def test_profile_button_opens_login_form(self, driver, wait):
        # Вход через кнопку «Личный кабинет»
        main = MainPage(driver, wait)
        main.open_main()
        main.click_profile_header()
        login_page = LoginPage(driver, wait)
        assert login_page.is_login_form_visible()

    def test_login_via_registration_form(self, driver, wait):
        # Вход через кнопку в форме регистрации
        main = MainPage(driver, wait)
        main.open_main()
        main.click_login_header()
        RegisterPage(driver, wait).go_to_register()
        LoginPage(driver, wait).go_to_login()
        LoginPage(driver, wait).login(TEST_USER["email"], TEST_USER["password"])
        profile = ProfilePage(driver, wait)
        assert profile.is_logged_in()

    def test_login_via_password_recovery(self, driver, wait):
        # Вход через кнопку в форме восстановления пароля
        main = MainPage(driver, wait)
        main.open_main()
        main.click_login_header()
        RecoveryPage(driver, wait).go_to_password_recovery()
        LoginPage(driver, wait).go_to_login()
        LoginPage(driver, wait).login(TEST_USER["email"], TEST_USER["password"])
        profile = ProfilePage(driver, wait)
        assert profile.is_logged_in()
