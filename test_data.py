import random
import string

# Тестовые данные. Аккаунт нужно зарегистрировать на стенде один раз вручную.
TEST_USER = {
    "name": "Test Testov",
    "email": "test_testov_2026_123@yandex.ru",  # ЗАМЕНИТЬ по восстановлению стенда на реальный email
    "password": "12345678",                     # ЗАМЕНИТЬ по восстановлению стенда на реальный пароль
}


def generate_email(first_name, last_name, cohort):
    # Генерирует уникальный email: имя_фамилия_когорта_3цифры@домен
    digits = "".join(random.choices(string.digits, k=3))
    name_part = f"{first_name.lower()}_{last_name.lower()}_{cohort}_{digits}"
    return f"{name_part}@yandex.ru"


def generate_password(length=8):
    # Генерирует случайный валидный пароль из букв и цифр
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))
