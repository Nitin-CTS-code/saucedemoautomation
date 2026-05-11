#define action like click, type, enter
#define methods to find locaters //make them easy
#define conditiions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )
    
    def enter_text(self,locator,text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)        

    def click(self,locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()
        
        # element = self.find(locator)
        # element.click()

    def get_text(self, locator):
        return self.find(locator).text