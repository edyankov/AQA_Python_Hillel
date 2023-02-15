from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_get_random_id(driver_browser, get_random_id):
    web_element_id = driver_browser.find_element(By.XPATH, f'//p[@id="{get_random_id}"]')
    assert "random" in web_element_id.text


def test_wait_for_enable_button(driver_browser):
    enable_button = driver_browser.find_element(By.ID, 'enableAfter')
    wait_for_element_to_become_clickable(driver_browser, 'enableAfter')
    assert enable_button.is_enabled()


def test_present_button(driver_browser):
    driver_browser.refresh()
    wait_for_element_to_become_visible(driver_browser, 'visibleAfter')
    visible_button = driver_browser.find_element(By.ID, 'visibleAfter')
    assert visible_button.is_displayed()


def wait_for_element_to_become_visible(driver_browser, element_id: str) -> None:
    WebDriverWait(driver_browser, 6).until(ec.visibility_of_element_located((By.ID, element_id)))


def wait_for_element_to_become_clickable(driver_browser, element_id: str) -> None:
    WebDriverWait(driver_browser, 6).until(ec.element_to_be_clickable((By.ID, element_id)))
