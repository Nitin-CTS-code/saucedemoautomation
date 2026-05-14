from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from data.testdata import TestData

class loginPage(BasePage):
    # url = "https//www.google.com"
    def load(self):
        # self.driver.get("https://www.saucedemo.com/")
        self.driver.get(TestData.base_url)

    #locaters
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self,username,password):
        self.enter_text(self.USERNAME,username)
        self.enter_text(self.PASSWORD,password)
        self.click(self.LOGIN_BTN)

    def get_error(self):
        return self.get_text(self.ERROR_MSG)