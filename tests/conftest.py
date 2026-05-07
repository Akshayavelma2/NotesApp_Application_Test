#this is used for setup and teardown for testCasesS

import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.environment import config


@pytest.fixture
def driver():

    chrome_options = Options()

    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage") 
    chrome_options.add_argument("--disable-gpu") 
    chrome_options.add_argument("--window-size=1920,1080") #tis shows the size of the window

    if os.getenv("GRID") == "true":

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub", 
            options=chrome_options
        )

    else:

        driver = webdriver.Chrome( #opens chrome browser
            options=chrome_options 
        )

    driver.maximize_window()

    driver.get(config["url"])

    yield driver 

    driver.quit()