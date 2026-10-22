import pytest
from page_objects import MainPage
from conftest import generate_email, generate_password


@pytest.mark.registration
def test_successful_registration(driver, wait):
    # Успешная регистрация с уникальным email и валидным паролем
    main = MainPage(driver, wait).open_main()
    register_page = main.go_to_login().go_to_register()
    email = generate_email("Alexa", "Alisova", "2026")
    profile = register_page.register("Alexa", email, generate_password())
    assert profile.is_logged_in()


@pytest.mark.registration
def test_registration_invalid_password(driver, wait):
    # Ошибка при некорректном пароле (меньше шести символов)
    main = MainPage(driver, wait).open_main()
    register_page = main.go_to_login().go_to_register()
    email = generate_email("Alexa", "Alisova", "2026")
    register_page.register("Alexa", email, "abcde")
    error = register_page.get_error_message()
    assert error is not None
