import pytest
from page_objects import MainPage, ConstructorPage


@pytest.mark.constructor
def test_constructor_buns_tab(driver, wait):
    # Переход к разделу «Булки»
    page = MainPage(driver, wait).open_main()
    constructor = ConstructorPage(page.driver, page.wait)
    assert constructor.open_buns_tab().has_ingredient_card()


@pytest.mark.constructor
def test_constructor_sauces_tab(driver, wait):
    # Переход к разделу «Соусы»
    page = MainPage(driver, wait).open_main()
    constructor = ConstructorPage(page.driver, page.wait)
    assert constructor.open_sauces_tab().has_ingredient_card()


@pytest.mark.constructor
def test_constructor_ingredients_tab(driver, wait):
    # Переход к разделу «Начинки»
    page = MainPage(driver, wait).open_main()
    constructor = ConstructorPage(page.driver, page.wait)
    assert constructor.open_ingredients_tab().has_ingredient_card()
