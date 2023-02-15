import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="session")
def driver():
    with Chrome() as driver:
        yield driver


@pytest.fixture()
def checkbox_page(driver):
    driver.get("https://demoqa.com/checkbox")
    yield
    driver.quit()
