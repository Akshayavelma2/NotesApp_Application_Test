#it is for all common methods

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
#self is used for instance of class
    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )
#locator is for finding element
    def find(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator):

        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )
#to send values to input fields
    def type(self, locator, value):

        element = self.find(locator)

        element.clear()

        element.send_keys(value)