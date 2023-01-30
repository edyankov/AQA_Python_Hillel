from selenium.webdriver.common.by import By

FULL_NAME_FIELD = '#userName'
EMAIL_FIELD = '#userEmail'
CURRENT_ADDRESS_FIELD = '#currentAddress'
PERMANENT_ADDRESS_FIELD = '#permanentAddress'
SUBMIT_BUTTON = '#submit'

OUTPUT_RESULT_NAME_ROW = '#name'
OUTPUT_RESULT_EMAIL_ROW = '#email'
OUTPUT_RESULT_CURRENT_ADDRESS_ROW = 'p#currentAddress'
OUTPUT_RESULT_PERMANENT_ADDRESS_ROW = 'p#permanentAddress'

ERROR_COLOR_EMAIL_FIELD_BORDER = '#userEmail.field-error'


class TestTextBox:

    def test_output_data_after_submit_css(self, open_demo_qa):
        full_name_input_field = open_demo_qa.find_element(By.CSS_SELECTOR, FULL_NAME_FIELD)
        email_input_field = open_demo_qa.find_element(By.CSS_SELECTOR, EMAIL_FIELD)
        current_address_input_field = open_demo_qa.find_element(By.CSS_SELECTOR, CURRENT_ADDRESS_FIELD)
        permanent_address_input_field = open_demo_qa.find_element(By.CSS_SELECTOR, PERMANENT_ADDRESS_FIELD)
        submit_button = open_demo_qa.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON)

        full_name_input_field.send_keys("My Full Name")
        email_input_field.send_keys("test@gmail.com")
        current_address_input_field.send_keys("My current address")
        permanent_address_input_field.send_keys("My permanent address")

        value_name = full_name_input_field.get_attribute("value")
        value_email = email_input_field.get_attribute("value")
        value_current_address = current_address_input_field.get_attribute("value")
        value_permanent_address = permanent_address_input_field.get_attribute("value")

        open_demo_qa.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        result_name = open_demo_qa.find_element(By.CSS_SELECTOR, OUTPUT_RESULT_NAME_ROW).text.split(':')[1]
        result_email = open_demo_qa.find_element(By.CSS_SELECTOR, OUTPUT_RESULT_EMAIL_ROW).text.split(':')[1]
        result_current_address = open_demo_qa.find_element(By.CSS_SELECTOR,
                                                           OUTPUT_RESULT_CURRENT_ADDRESS_ROW).text.split(':')[1]
        result_permanent_address = open_demo_qa.find_element(By.CSS_SELECTOR,
                                                             OUTPUT_RESULT_PERMANENT_ADDRESS_ROW).text.split(':')[1]

        output_data_after_submit = [result_name == value_name, result_email == value_email,
                                    result_current_address == value_current_address,
                                    result_permanent_address == value_permanent_address]
        assert all(output_data_after_submit)

    def test_validation_email_field(self, open_demo_qa):
        email_input_field = open_demo_qa.find_element(By.CSS_SELECTOR, EMAIL_FIELD)
        submit_button = open_demo_qa.find_element(By.CSS_SELECTOR, SUBMIT_BUTTON)

        email_input_field.send_keys("testgmail.com")

        open_demo_qa.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        validation_email_border_color = open_demo_qa.find_element(By.CSS_SELECTOR, ERROR_COLOR_EMAIL_FIELD_BORDER)

        assert validation_email_border_color
