import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('get_browser')
class TestPageLinks:

    def test_amount_home_links_on_page(self):
        amount_home_links = self.driver.find_elements(By.XPATH, '//div[@id="linkWrapper"]//a[text()="Home"]')
        assert len(amount_home_links) == 2
        for link in amount_home_links:
            assert link.is_displayed()  # if Home links are not displayed on the page
