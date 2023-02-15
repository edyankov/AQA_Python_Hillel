import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver_browser():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/checkbox")
    yield driver
    driver.quit()

