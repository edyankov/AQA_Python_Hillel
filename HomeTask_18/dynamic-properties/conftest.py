import pytest
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def dynamic_properties_page(request):
    driver = request.getfixturevalue("driver_browser")
    driver.get("https://demoqa.com/dynamic-properties")
    yield driver


@pytest.fixture(scope='function')
def get_random_id(driver_browser):
    random_id = driver_browser.find_element(By.XPATH, '//p[contains(text(), "random")]')
    yield random_id.get_attribute('id')
