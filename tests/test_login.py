import pytest
from pages import login_page
from pages.login_page import loginPage
# from driversetup.driverfactory import DriverFactory
from data.testdata import TestData


def test_valid_login(driver):
    Login = loginPage(driver)
    Login.load()
    Login.login(
        TestData.valid_creds["username"],
        TestData.valid_creds["password"]
        )
    
    # folder_path = r"C:\Users\User\Desktop\Automation\screenshots"
    filename = "valid.png"
    file_path = TestData.folder_path + "\\" + filename  # manual path join
    driver.save_screenshot(file_path)


    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    Login = loginPage(driver)
    Login.load()
    Login.login(
        TestData.invalid_creds["username"],
        TestData.invalid_creds["password"]
    )

    # folder_path = r"C:\Users\User\Desktop\Automation\screenshots"
    filename = "invalid_login.png"
    file_path = TestData.folder_path + "\\" + filename  # manual path join
    driver.save_screenshot(file_path)

    assert "Epic sadface" in Login.get_error()

def test_locker_user(driver):
    Login = loginPage(driver)
    Login.load()
    Login.login(
        TestData.locked_cred["username"],
        TestData.locked_cred["password"]
    )
    # folder_path = r"C:\Users\User\Desktop\Automation\screenshots"
    filename = "locker_user.png"
    file_path = TestData.folder_path + "//" + filename
    driver.save_screenshot(file_path)

    assert "Epic sadface: Sorry, this user has been locked out." in Login.get_error()