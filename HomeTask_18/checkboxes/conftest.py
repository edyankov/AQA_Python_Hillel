import pytest


@pytest.fixture(scope="session")
def checkbox_page(request):
    driver = request.getfixturevalue("driver_browser")
    driver.get("https://demoqa.com/checkbox")
    yield driver
