from selenium import webdriver

class DriverFactory:

    @staticmethod
    def get_driver(browser_name):
        if browser_name.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(options=options)

        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox()

        else:
            raise Exception(f"Browser {browser_name} not supported")