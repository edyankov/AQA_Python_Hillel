import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def get_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-setuid-sandbox")
    return options


@pytest.fixture
def driver_chrome(get_options):
    options = get_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture
def chrome(request, driver_chrome):
    driver = driver_chrome
    if request.cls is not None:
        request.cls.driver = driver
    driver.get('https://demoqa.com/books')
    yield driver
    driver.quit()
