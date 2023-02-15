from selenium.webdriver.common.by import By


def test_activate_yes_radio_first(driver, radio_button_page):
    rad_button_yes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    rad_button_yes_input = driver.find_element(By.XPATH, '//input[@id="yesRadio"]')
    rad_button_yes.click()
    result_text = driver.find_element(By.XPATH, '//span[@class="text-success"]').text
    assert all([result_text == "Yes", rad_button_yes_input.is_enabled()])


def test_get_radio_buttons_info(driver, radio_button_page):
    radio_button_names = driver.find_elements(By.XPATH, '//label[contains(@class, "custom-control")]')
    radio_button_states = driver.find_elements(By.XPATH, '//input[@type="radio"]')
    radio_buttons_dict = {}
    for i, radio_button_name in enumerate(radio_button_names):
        radio_buttons_dict[radio_button_name.text] = {
            'enabled': radio_button_states[i].is_enabled(),
            'selected': radio_button_states[i].is_selected()
        }
    assert len(radio_button_names) == len(radio_button_states) == len(radio_buttons_dict)


def test_activate_disabled_radio_button(driver, radio_button_page):
    rad_button_no_label = driver.find_element(By.XPATH, '//label[@for="noRadio"]')
    rad_button_no_input = driver.find_element(By.XPATH, '//input[@id="noRadio"]')
    driver.execute_script(
        "arguments[0].removeAttribute('disabled','disabled')", rad_button_no_input)
    rad_button_no_label.click()
    assert rad_button_no_input.is_selected()
