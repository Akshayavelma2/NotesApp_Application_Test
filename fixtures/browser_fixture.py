#Fixture is used for setup and teardoen browser or testcases
#browser fixture is used for setup and teardown of browser for test cases
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.environment import config


@pytest.fixture
def driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    driver.get(config["url"])
#yield is used for instance of class
    yield driver

    driver.quit()