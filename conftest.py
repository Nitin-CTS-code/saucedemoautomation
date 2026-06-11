#setup reusable code here
import pytest
from pages.login_page import loginPage
from driversetup.driverfactory import DriverFactory


#driver
@pytest.fixture
def driver():
    driver = DriverFactory.get_driver("chrome")
    yield driver
    driver.quit()

#login
@pytest.fixture
def performLogin(driver):

    login = loginPage(driver)

    login.load()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    return driver
# @pytest.fixture
# def performLogin(driver):
#     login = loginPage(driver)
#     loginPage.load()
#     loginPage.login("standard_user","secret_sauce")
    