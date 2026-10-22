import pytest

from page_objects import MainPage, LoginPage, ProfilePage, ConstructorPage
from test_data import TEST_USER


@pytest.mark.navigation
class TestProfileNavigation:
    def test_go_to_profile_from_main(self, driver, wait):
        # Переход в личный кабинет по клику на «Личный кабинет»
        # (без логина открывается форма входа)
        main = MainPage(driver, wait)
        main.open_main()
        main.click_profile_header()
        login_page = LoginPage(driver, wait)
        assert login_page.is_login_form_visible()

    def test_logout_from_personal_cabinet(self, driver, wait):
        # Выход из аккаунта по кнопке «Выйти»:
        # после выхода снова видна кнопка «Войти в аккаунт»
        main = MainPage(driver, wait)
        main.open_main()
        main.click_login_header()
        LoginPage(driver, wait).login(TEST_USER["email"], TEST_USER["password"])
        ProfilePage(driver, wait).logout()
        main_page = MainPage(driver, wait)
        assert main_page.is_login_button_visible()

    def test_go_to_constructor_from_profile(self, driver, wait):
        # Переход из личного кабинета в конструктор по клику на «Конструктор»
        main = MainPage(driver, wait)
        main.open_main()
        main.click_login_header()
        LoginPage(driver, wait).login(TEST_USER["email"], TEST_USER["password"])
        ProfilePage(driver, wait).go_to_constructor()
        constructor = ConstructorPage(driver, wait)
        assert constructor.has_ingredient_card()

    def test_go_to_constructor_via_logo(self, driver, wait):
        # Переход из личного кабинета в конструктор по клику на логотип:
        # входим, попадаем в ЛК, в конструктор и по логотипу на главную
        main = MainPage(driver, wait)
        main.open_main()
        main.click_login_header()
        LoginPage(driver, wait).login(TEST_USER["email"], TEST_USER["password"])
        ProfilePage(driver, wait).go_to_constructor()
        main_page = MainPage(driver, wait)
        main_page.click_logo()
        assert ConstructorPage(driver, wait).has_ingredient_card()
