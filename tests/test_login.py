import pytest
from page_objects import MainPage
from conftest import TEST_USER


@pytest.mark.login
def test_login_via_main_page(driver, wait):
    # Вход по кнопке «Войти в аккаунт» на главной
    login_page = MainPage(driver, wait).open_main().go_to_login()
    profile = login_page.login(TEST_USER["email"], TEST_USER["password"])
    assert profile.is_logged_in()


@pytest.mark.login
def test_login_via_profile_button(driver, wait):
    # Вход через кнопку «Личный кабинет»
    login_page = MainPage(driver, wait).open_main().go_to_profile()
    assert login_page.is_login_form_visible()
    profile = login_page.login(TEST_USER["email"], TEST_USER["password"])
    assert profile.is_logged_in()


@pytest.mark.login
def test_login_via_registration_form(driver, wait):
    # Вход через кнопку в форме регистрации
    main = MainPage(driver, wait).open_main()
    register_page = main.go_to_login().go_to_register()
    login_page = register_page.go_to_login()
    profile = login_page.login(TEST_USER["email"], TEST_USER["password"])
    assert profile.is_logged_in()


@pytest.mark.login
def test_login_via_password_recovery(driver, wait):
    # Вход через кнопку в форме восстановления пароля
    main = MainPage(driver, wait).open_main()
    recovery_page = main.go_to_login().go_to_password_recovery()
    login_page = recovery_page.go_to_login()
    profile = login_page.login(TEST_USER["email"], TEST_USER["password"])
    assert profile.is_logged_in()
