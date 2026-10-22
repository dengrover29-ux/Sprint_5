import pytest
from page_objects import MainPage, ConstructorPage
from conftest import TEST_USER


@pytest.mark.navigation
def test_go_to_profile_from_main(driver, wait):
    # Переход в личный кабинет по клику на «Личный кабинет»
    # (без логина открывается форма входа)
    login_page = MainPage(driver, wait).open_main().go_to_profile()
    assert login_page.is_login_form_visible()


@pytest.mark.navigation
def test_logout_from_personal_cabinet(driver, wait):
    # Выход из аккаунта по кнопке «Выйти»:
    # после выхода снова видна кнопка «Войти в аккаунт»
    main = MainPage(driver, wait).open_main()
    profile = main.go_to_login().login(TEST_USER["email"], TEST_USER["password"])
    main_page = profile.logout()
    assert main_page.is_login_form_visible()


@pytest.mark.navigation
def test_go_to_constructor_from_profile(driver, wait):
    # Переход из личного кабинета в конструктор по клику на «Конструктор»
    main = MainPage(driver, wait).open_main()
    profile = main.go_to_login().login(TEST_USER["email"], TEST_USER["password"])
    constructor = profile.go_to_constructor()
    assert constructor.has_ingredient_card()


@pytest.mark.navigation
def test_go_to_constructor_via_logo(driver, wait):
    # Переход из личного кабинета в конструктор по клику на логотип:
    # входим, попадаем в ЛК, в конструктор и по логотипу на главную
    main = MainPage(driver, wait).open_main()
    profile = main.go_to_login().login(TEST_USER["email"], TEST_USER["password"])
    constructor = profile.go_to_constructor()
    assert constructor.has_ingredient_card()
    main_page = MainPage(driver, wait)
    main_page.go_to_constructor_via_logo()
    assert constructor.has_ingredient_card()
