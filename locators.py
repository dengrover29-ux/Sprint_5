from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка «Войти в аккаунт» на главной
    HEADER_LINK_PROFILE = (By.XPATH, "//a[contains(text(), 'Личный кабинет')]")  # Кнопка «Личный кабинет» в шапке
    BURGER_LOGO = (By.CSS_SELECTOR, "a[href='/']")  # Логотип Stellar Burgers


class LoginPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")  # Поле Email в форме входа
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")  # Поле Пароль в форме входа
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")  # Кнопка «Войти» в форме входа
    REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")  # Ссылка «Зарегистрироваться» под формой входа
    RECOVER_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")  # Ссылка «Восстановить пароль»
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")  # Блок с сообщением об ошибке


class RegisterPageLocators:
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")  # Поле Имя в форме регистрации
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")  # Поле Email в форме регистрации
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")  # Поле Пароль в форме регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка «Зарегистрироваться»
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")  # Ссылка «Войти» под формой регистрации
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")  # Блок с ошибкой (некорректный пароль)


class RecoveryPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")  # Ссылка «Войти» на странице восстановления пароля


class ProfilePageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")  # Кнопка «Выйти» в личном кабинете
    CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(text(), 'Конструктор')]")  # Ссылка «Конструктор» в шапке


class ConstructorPageLocators:
    TAB_BUNS = (By.XPATH, "//div[contains(text(), 'Булки')]")  # Вкладка «Булки»
    TAB_SAUCES = (By.XPATH, "//div[contains(text(), 'Соусы')]")  # Вкладка «Соусы»
    TAB_INGREDIENTS = (By.XPATH, "//div[contains(text(), 'Начинки')]")  # Вкладка «Начинки»
    INGREDIENT_CARD = (By.CSS_SELECTOR, "div[class*='BurgerIngredient']")  # Карточка ингредиента
