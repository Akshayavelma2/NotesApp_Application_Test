#it gves the performance of api and ui

import time
import requests

from config.environment import load_config


config = load_config()

BASE_URL = config["api_url"]

#it gives api response time
def test_api_response_time():

    start_time = time.time()

    response = requests.get(
        f"{BASE_URL}/notes"
    )

    end_time = time.time()

    response_time = end_time - start_time

    print(
        f"\nAPI Response Time: "
        f"{round(response_time, 2)} seconds"
    )

    assert response_time < 15



#it gives ui response time
def test_ui_page_load_time(driver):

    start_time = time.time()

    driver.get(
        config["url"]
    )

    for i in range(10):

        dom_state = driver.execute_script(
            "return document.readyState"
        )

        if dom_state == "complete":
            break

        time.sleep(1)

    end_time = time.time()

    load_time = end_time - start_time

    print(
        f"\nUI Page Load Time: "
        f"{round(load_time, 2)} seconds"
    )

    assert load_time < 60