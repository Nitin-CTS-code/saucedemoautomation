import pytest
from pages import login_page
from pages.login_page import loginPage
from driversetup.driverfactory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver("chrome")
    yield driver
    driver.quit()


def test_valid_login(driver):
    Login = loginPage(driver)
    Login.load()
    Login.login("standard_user","secret_sauce")

    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    Login = loginPage(driver)
    Login.load()
    Login.login("adsadasdasdd","asdasdsadsadsad")

    assert "Epic sadface" in Login.get_error()