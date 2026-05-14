import pytest
from pages import login_page
from pages.login_page import loginPage
from driversetup.driverfactory import DriverFactory
from data.testdata import TestData


@pytest.fixture
def driver():
    driver = DriverFactory.get_driver("chrome")
    yield driver
    driver.quit()


def test_valid_login(driver):
    Login = loginPage(driver)
    Login.load()
    Login.login(
        TestData.valid_creds["username"],
        TestData.valid_creds["password"]
        )
    folder_path = r"C:\Users\User\Desktop\Automation\screenshots"
    filename = "valid.png"
    file_path = folder_path + "\\" + filename  # manual path join
    driver.save_screenshot(file_path)


    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    Login = loginPage(driver)
    Login.load()
    Login.login(
        TestData.invalid_creds["username"],
        TestData.invalid_creds["password"]
    )

    folder_path = r"C:\Users\User\Desktop\Automation\screenshots"
    filename = "invalid_login.png"
    file_path = folder_path + "\\" + filename  # manual path join
    driver.save_screenshot(file_path)

    assert "Epic sadface" in Login.get_error()