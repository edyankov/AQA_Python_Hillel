import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
