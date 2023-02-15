import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def driver_browser():
    driver = webdriver.Chrome()
    try:
        driver.get("https://demoqa.com/dynamic-properties")
        yield driver
    finally:
        driver.quit()


@pytest.fixture(scope='function')
def get_random_id(driver_browser):
    random_id = driver_browser.find_element(By.XPATH, '//p[contains(text(), "random")]')
    yield random_id.get_attribute('id')
