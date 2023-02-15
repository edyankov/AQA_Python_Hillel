import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver_browser():
    driver = webdriver.Chrome()
    try:
        driver.get("https://demoqa.com/radio-button")
        yield driver
    finally:
        driver.quit()
