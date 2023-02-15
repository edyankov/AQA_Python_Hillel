from selenium.webdriver.common.by import By


def expand_folder_tree(driver, folder_tree):
    for folder in folder_tree:
        expand_button = driver.find_element(
            By.XPATH, f'//span[@class="rct-text"][.="{folder}"]/button[@aria-label="Toggle"]')
        _ = expand_button.location_once_scrolled_into_view
        expand_button.click()


def select_checkboxes(driver, checkboxes):
    for checkbox in checkboxes:
        checkbox_element = driver.find_element(
            By.XPATH, f'//span[@class="rct-title"][.="{checkbox}"]//ancestor::label')
        _ = checkbox_element.location_once_scrolled_into_view
        checkbox_input = checkbox_element.find_element(By.CSS_SELECTOR, "input[id]")
        if not checkbox_input.is_selected():
            checkbox_element.click()


def test_checkboxes(driver_browser):
    folder_tree = ["Home", "Desktop", "Documents", "WorkSpace", "Office", "Downloads"]
    expand_folder_tree(driver_browser, folder_tree)
    checkboxes = ["Commands", "General"]
    select_checkboxes(driver_browser, checkboxes)
    result_element = driver_browser.find_element(By.XPATH, '//div[@id="result"]')
    result_text = result_element.text.split(":")[1].split()
    expected_results = [checkbox.lower() for checkbox in checkboxes]
    assert result_text == expected_results
