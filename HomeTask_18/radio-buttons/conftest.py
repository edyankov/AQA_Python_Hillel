import pytest


@pytest.fixture(scope="session")
def radio_button_page(request):
    driver = request.getfixturevalue("driver_browser")
    driver.get("https://demoqa.com/radio-button")
    yield driver
