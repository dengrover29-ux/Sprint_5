import pytest

from page_objects import MainPage, ConstructorPage
from locators import ConstructorPageLocators


@pytest.mark.constructor
class TestConstructorTabs:
    def test_constructor_buns_tab(self, driver, wait):
        # Переход к разделу «Булки»: проверяем класс активного таба
        MainPage(driver, wait).open_main()
        constructor = ConstructorPage(driver, wait)
        constructor.click_buns_tab()
        assert constructor.is_tab_active(ConstructorPageLocators.TAB_BUNS)

    def test_constructor_sauces_tab(self, driver, wait):
        # Переход к разделу «Соусы»: проверяем класс активного таба
        MainPage(driver, wait).open_main()
        constructor = ConstructorPage(driver, wait)
        constructor.click_sauces_tab()
        assert constructor.is_tab_active(ConstructorPageLocators.TAB_SAUCES)

    def test_constructor_ingredients_tab(self, driver, wait):
        # Переход к разделу «Начинки»: проверяем класс активного таба
        MainPage(driver, wait).open_main()
        constructor = ConstructorPage(driver, wait)
        constructor.click_ingredients_tab()
        assert constructor.is_tab_active(ConstructorPageLocators.TAB_INGREDIENTS)
