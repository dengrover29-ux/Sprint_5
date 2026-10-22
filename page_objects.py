from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from constants import BASE_URL
from locators import (MainPageLocators, LoginPageLocators, RegisterPageLocators,
                      RecoveryPageLocators, ProfilePageLocators, ConstructorPageLocators)


class BasePage:
    """Все прямые обращения к driver и wait живут только здесь.
    Объекты страниц используют только методы BasePage."""

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=20):
        # Таймаут передаётся в WebDriverWait: короткие проверки не висят по 15 секунд
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        el = self.wait_for_element(locator)
        el.click()

    def input_text(self, locator, text):
        el = self.wait_for_element(locator)
        el.clear()
        el.send_keys(text)

    def is_element_visible(self, locator, timeout=10):
        try:
            self.wait_for_element(locator, timeout)
            return True
        except TimeoutException:
            return False

    def get_attribute(self, locator, attribute):
        return self.wait_for_element(locator).get_attribute(attribute)


class MainPage(BasePage):
    def open_main(self):
        self.open_url(BASE_URL)

    def click_login_header(self):
        self.click_element(MainPageLocators.HEADER_BUTTON_LOGIN)

    def click_profile_header(self):
        self.click_element(MainPageLocators.HEADER_LINK_PROFILE)

    def click_logo(self):
        # Клик по логотипу Stellar Burgers возвращает на главную
        self.click_element(MainPageLocators.BURGER_LOGO)

    def is_login_button_visible(self):
        return self.is_element_visible(MainPageLocators.HEADER_BUTTON_LOGIN)


class LoginPage(BasePage):
    def login(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    def go_to_register(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)

    def go_to_password_recovery(self):
        self.click_element(LoginPageLocators.RECOVER_LINK)

    def is_login_form_visible(self):
        return self.is_element_visible(LoginPageLocators.EMAIL_INPUT)

    def get_error_message(self):
        try:
            el = self.wait_for_element(LoginPageLocators.ERROR_MESSAGE, timeout=5)
            return el.text
        except TimeoutException:
            return None


class RegisterPage(BasePage):
    def register(self, name, email, password):
        self.input_text(RegisterPageLocators.NAME_INPUT, name)
        self.input_text(RegisterPageLocators.EMAIL_INPUT, email)
        self.input_text(RegisterPageLocators.PASSWORD_INPUT, password)
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    def go_to_login(self):
        self.click_element(RegisterPageLocators.LOGIN_LINK)

    def get_error_message(self):
        # Ожидание элемента внутри метода: вызывается прямо в assert теста
        try:
            el = self.wait_for_element(RegisterPageLocators.ERROR_MESSAGE, timeout=5)
            return el.text
        except TimeoutException:
            return None


class RecoveryPage(BasePage):
    def go_to_login(self):
        self.click_element(RecoveryPageLocators.LOGIN_LINK)


class ProfilePage(BasePage):
    def is_logged_in(self):
        return self.is_element_visible(ProfilePageLocators.LOGOUT_BUTTON)

    def logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)

    def go_to_constructor(self):
        self.click_element(ProfilePageLocators.CONSTRUCTOR_LINK)


class ConstructorPage(BasePage):
    def click_buns_tab(self):
        self.click_element(ConstructorPageLocators.TAB_BUNS)

    def click_sauces_tab(self):
        self.click_element(ConstructorPageLocators.TAB_SAUCES)

    def click_ingredients_tab(self):
        self.click_element(ConstructorPageLocators.TAB_INGREDIENTS)

    def is_tab_active(self, locator):
        # При активации табу добавляется класс tab_type_current - проверяем его
        classes = self.get_attribute(locator, "class")
        return ConstructorPageLocators.TAB_ACTIVE_CLASS in classes

    def has_ingredient_card(self):
        return self.is_element_visible(ConstructorPageLocators.INGREDIENT_CARD, timeout=10)
