import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

# Тестовый аккаунт для проверки входа. Зарегистрируй его на стенде один раз
# вручную и подставь реальные email и пароль - иначе тесты входа упадут.
TEST_USER = {
    "name": "Test Testov",
    "email": "test_testov_2026_123@yandex.ru",  # ЗАМЕНИТЬ по восстановлению стенда на реальный email
    "password": "12345678",                     # ЗАМЕНИТЬ по восстановлению стенда на реальный пароль
}


def generate_email(first_name, last_name, cohort):
    # Генерирует уникальный email: имя_фамилия_когорта_3цифры@домен ЗАМЕНИТЬ по восстановлению стенда
    digits = "".join(random.choices(string.digits, k=3))
    name_part = f"{first_name.lower()}_{last_name.lower()}_{cohort}_{digits}"
    return f"{name_part}@yandex.ru"


def generate_password(length=8):
    # Генерирует случайный валидный пароль из букв и цифр
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


@pytest.fixture
def driver():
    # Ревью выполняется с Chrome, Firefox отключён
    d = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    d.set_window_size(1920, 1080)
    yield d
    d.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 15)
