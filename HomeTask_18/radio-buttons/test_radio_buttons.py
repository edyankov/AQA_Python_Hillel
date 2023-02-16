from selenium.webdriver.common.by import By


def test_activate_yes_radio_first(radio_button_page):
    radio_button_page.refresh()
    rad_button_yes = radio_button_page.find_element(By.XPATH, '//label[@for="yesRadio"]')
    rad_button_yes_input = radio_button_page.find_element(By.XPATH, '//input[@id="yesRadio"]')
    rad_button_yes.click()
    result_text = radio_button_page.find_element(By.XPATH, '//span[@class="text-success"]').text
    assert all([result_text == "Yes", rad_button_yes_input.is_enabled()])


def test_get_radio_buttons_info(radio_button_page):
    radio_button_page.refresh()
    radio_button_names = radio_button_page.find_elements(By.XPATH, '//label[contains(@class, "custom-control")]')
    radio_button_states = radio_button_page.find_elements(By.XPATH, '//input[@type="radio"]')
    radio_buttons_dict = {}
    for i, radio_button_name in enumerate(radio_button_names):
        radio_buttons_dict[radio_button_name.text] = {
            'enabled': radio_button_states[i].is_enabled(),
            'selected': radio_button_states[i].is_selected()
        }
    assert len(radio_button_names) == len(radio_button_states) == len(radio_buttons_dict)


def test_activate_disabled_radio_button(radio_button_page):
    radio_button_page.refresh()
    rad_button_no_label = radio_button_page.find_element(By.XPATH, '//label[@for="noRadio"]')
    rad_button_no_input = radio_button_page.find_element(By.XPATH, '//input[@id="noRadio"]')
    radio_button_page.execute_script(
        "arguments[0].removeAttribute('disabled','disabled')", rad_button_no_input)
    rad_button_no_label.click()
    assert rad_button_no_input.is_selected()
