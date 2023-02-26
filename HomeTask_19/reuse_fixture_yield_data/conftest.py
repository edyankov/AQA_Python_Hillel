""""Reuse fixture yield data": Створити 2 фікстури. Нехай одна буде створювати headless драйвер
(На ваш вибір: Chrome/Chromium/Edge, Firefox), а інша буде використовуючи цей драйвер відкривати
сторінку https://demoqa.com/links та закривати драйвер після тесту.
Створити тест, який переконається, що на сторінці є 2 посилання з текстом "Home".
Не викликати ЯВНО фікстуру в тесті (сигнатура тестової функції має бути пуста)."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def get_chrome_headless():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def get_browser(request, get_chrome_headless):
    driver = get_chrome_headless
    if request.cls is not None:
        request.cls.driver = driver
    try:
        driver.get('https://demoqa.com/links')
        yield
    finally:
        driver.quit()
