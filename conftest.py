import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait


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
