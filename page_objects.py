from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from locators import (MainPageLocators, LoginPageLocators, RegisterPageLocators,
                      RecoveryPageLocators, ProfilePageLocators, ConstructorPageLocators)


class BasePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

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


class MainPage(BasePage):
    def open_main(self):
        self.driver.get("https://stellarburgers.education-services.ru/")
        return self

    def go_to_login(self):
        self.click_element(MainPageLocators.HEADER_BUTTON_LOGIN)
        return LoginPage(self.driver, self.wait)

    def go_to_profile(self):
        self.click_element(MainPageLocators.HEADER_LINK_PROFILE)
        return LoginPage(self.driver, self.wait)

    def go_to_constructor_via_logo(self):
        # Клик по логотипу Stellar Burgers возвращает на главную
        self.click_element(MainPageLocators.BURGER_LOGO)
        return ConstructorPage(self.driver, self.wait)


class LoginPage(BasePage):
    def login(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_element(LoginPageLocators.LOGIN_BUTTON)
        return ProfilePage(self.driver, self.wait)

    def go_to_register(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)
        return RegisterPage(self.driver, self.wait)

    def go_to_password_recovery(self):
        self.click_element(LoginPageLocators.RECOVER_LINK)
        return RecoveryPage(self.driver, self.wait)

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
        return ProfilePage(self.driver, self.wait)

    def go_to_login(self):
        self.click_element(RegisterPageLocators.LOGIN_LINK)
        return LoginPage(self.driver, self.wait)

    def get_error_message(self):
        try:
            el = self.wait_for_element(RegisterPageLocators.ERROR_MESSAGE, timeout=5)
            return el.text
        except TimeoutException:
            return None


class RecoveryPage(BasePage):
    def go_to_login(self):
        self.click_element(RecoveryPageLocators.LOGIN_LINK)
        return LoginPage(self.driver, self.wait)


class ProfilePage(BasePage):
    def is_logged_in(self):
        return self.is_element_visible(ProfilePageLocators.LOGOUT_BUTTON)

    def logout(self):
        self.click_element(ProfilePageLocators.LOGOUT_BUTTON)
        return MainPage(self.driver, self.wait)

    def go_to_constructor(self):
        self.click_element(ProfilePageLocators.CONSTRUCTOR_LINK)
        return ConstructorPage(self.driver, self.wait)


class ConstructorPage(BasePage):
    def open_buns_tab(self):
        self.click_element(ConstructorPageLocators.TAB_BUNS)
        return self

    def open_sauces_tab(self):
        self.click_element(ConstructorPageLocators.TAB_SAUCES)
        return self

    def open_ingredients_tab(self):
        self.click_element(ConstructorPageLocators.TAB_INGREDIENTS)
        return self

    def has_ingredient_card(self):
        return self.is_element_visible(ConstructorPageLocators.INGREDIENT_CARD, timeout=10)
