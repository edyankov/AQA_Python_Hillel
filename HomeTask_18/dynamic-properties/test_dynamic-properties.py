from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_get_random_id(dynamic_properties_page, get_random_id):
    web_element_id = dynamic_properties_page.find_element(By.XPATH, f'//p[@id="{get_random_id}"]')
    assert "random" in web_element_id.text


def test_wait_for_enable_button(dynamic_properties_page):
    enable_button = dynamic_properties_page.find_element(By.ID, 'enableAfter')
    wait_for_element_to_become_clickable(dynamic_properties_page, 'enableAfter')
    assert enable_button.is_enabled()


def test_present_button(dynamic_properties_page):
    dynamic_properties_page.refresh()
    wait_for_element_to_become_visible(dynamic_properties_page, 'visibleAfter')
    visible_button = dynamic_properties_page.find_element(By.ID, 'visibleAfter')
    assert visible_button.is_displayed()


def wait_for_element_to_become_visible(dynamic_properties_page, element_id: str) -> None:
    WebDriverWait(dynamic_properties_page, 6).until(ec.visibility_of_element_located((By.ID, element_id)))


def wait_for_element_to_become_clickable(dynamic_properties_page, element_id: str) -> None:
    WebDriverWait(dynamic_properties_page, 6).until(ec.element_to_be_clickable((By.ID, element_id)))
