from selenium.webdriver.common.by import By
from conftest import driver


def expand_folder_tree(driver, folder_tree):
    for folder in folder_tree:
        expand_button = driver.find_element(
            By.XPATH, f'//span[@class="rct-text"][.="{folder}"]/button[@aria-label="Toggle"]')
        expand_button.click()


def select_checkboxes(driver, checkboxes):
    for checkbox in checkboxes:
        checkbox_element = driver.find_element(
            By.XPATH, f'//span[@class="rct-title"][.="{checkbox}"]')
        var = checkbox_element.location_once_scrolled_into_view
        checkbox_input = var.find_element(By.CSS_SELECTOR, "input[id]")
        if not checkbox_input.is_selected():
            var.click()


def test_checkboxes(checkbox_page):
    folder_tree = ["Home", "Desktop", "Documents", "WorkSpace", "Office", "Downloads"]
    expand_folder_tree(driver, folder_tree)
    checkboxes = ["Commands", "General"]
    select_checkboxes(driver, checkboxes)
    result_element = driver.find_element(By.XPATH, '//div[@id="result"]')
    result_text = result_element.text.split(":")[1].split()
    expected_results = [checkbox.lower() for checkbox in checkboxes]
    assert result_text == expected_results
