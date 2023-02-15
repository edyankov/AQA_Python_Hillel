import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="function")
def driver():
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def radio_button_page(driver):
    driver.get("https://demoqa.com/radio-button")
    yield driver
