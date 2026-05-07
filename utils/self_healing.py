from selenium.common.exceptions import NoSuchElementException


def find_with_self_healing(driver, locators):

    last_exception = None

    for locator in locators:
        try:
            return driver.find_element(*locator)

        except NoSuchElementException as error:
            last_exception = error

    raise last_exception