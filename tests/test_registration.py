import pytest

from page_objects import MainPage, RegisterPage, ProfilePage
from test_data import generate_email, generate_password


@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(self, driver, wait):
        # Успешная регистрация с уникальным email и валидным паролем
        main = MainPage(driver, wait)
        main.open_main()
        main.click_login_header()
        register_page = RegisterPage(driver, wait)
        register_page.go_to_register()
        email = generate_email("Alexa", "Alisova", "2026")
        register_page.register("Alexa", email, generate_password())
        profile = ProfilePage(driver, wait)
        assert profile.is_logged_in()

    def test_registration_invalid_password(self, driver, wait):
        # Ошибка при некорректном пароле (меньше шести символов).
        # Взаимодействие с элементом-маркером ошибки - только внутри ассерта:
        # ожидание появления элемента происходит внутри get_error_message
        main = MainPage(driver, wait)
        main.open_main()
        main.click_login_header()
        register_page = RegisterPage(driver, wait)
        register_page.go_to_register()
        email = generate_email("Alexa", "Alisova", "2026")
        register_page.register("Alexa", email, "abcde")
        assert register_page.get_error_message() is not None
