from selenium.webdriver.common.by import By

FULL_NAME_FIELD = '//input[@id="userName"]'
EMAIL_FIELD = '//input[@id="userEmail"]'
CURRENT_ADDRESS_FIELD = '//textarea[@id="currentAddress"]'
PERMANENT_ADDRESS_FIELD = '//textarea[@id="permanentAddress"]'
SUBMIT_BUTTON = '//button[@id="submit"]'

OUTPUT_RESULT_NAME_ROW = '//p[@id="name"]'
OUTPUT_RESULT_EMAIL_ROW = '//p[@id="email"]'
OUTPUT_RESULT_CURRENT_ADDRESS_ROW = '//p[@id="currentAddress"]'
OUTPUT_RESULT_PERMANENT_ADDRESS_ROW = '//p[@id="permanentAddress"]'

ERROR_COLOR_EMAIL_FIELD_BORDER = '//input[@id="userEmail"][contains(@class, "field-error")]'


class TestTextBox:

    def test_output_data_after_submit_xpath(self, open_demo_qa):
        full_name_input_field = open_demo_qa.find_element(By.XPATH, FULL_NAME_FIELD)
        email_input_field = open_demo_qa.find_element(By.XPATH, EMAIL_FIELD)
        current_address_input_field = open_demo_qa.find_element(By.XPATH, CURRENT_ADDRESS_FIELD)
        permanent_address_input_field = open_demo_qa.find_element(By.XPATH, PERMANENT_ADDRESS_FIELD)
        submit_button = open_demo_qa.find_element(By.XPATH, SUBMIT_BUTTON)

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

        result_name = open_demo_qa.find_element(By.XPATH, OUTPUT_RESULT_NAME_ROW).text.split(':')[1]
        result_email = open_demo_qa.find_element(By.XPATH, OUTPUT_RESULT_EMAIL_ROW).text.split(':')[1]
        result_current_address = open_demo_qa.find_element(By.XPATH,
                                                           OUTPUT_RESULT_CURRENT_ADDRESS_ROW).text.split(':')[1]
        result_permanent_address = open_demo_qa.find_element(By.XPATH,
                                                             OUTPUT_RESULT_PERMANENT_ADDRESS_ROW).text.split(':')[1]

        output_data_after_submit = [result_name == value_name, result_email == value_email,
                                    result_current_address == value_current_address,
                                    result_permanent_address == value_permanent_address]
        assert all(output_data_after_submit)

    def test_validation_email_field(self, open_demo_qa):
        email_input_field = open_demo_qa.find_element(By.XPATH, EMAIL_FIELD)
        submit_button = open_demo_qa.find_element(By.XPATH, SUBMIT_BUTTON)

        email_input_field.send_keys("testgmail.com")

        open_demo_qa.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        validation_email_color = open_demo_qa.find_element(By.XPATH, ERROR_COLOR_EMAIL_FIELD_BORDER)

        assert validation_email_color
