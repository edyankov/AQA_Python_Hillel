import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def open_demo_qa():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/text-box')
    yield driver
    driver.quit()
