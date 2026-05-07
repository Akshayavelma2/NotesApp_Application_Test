#thi is used for deleting the notes

import time
from pages.login_page import LoginPage
from pages.home_page import HomePage
from api.api_client import APIClient
from config.environment import config


def test_delete_note_api_to_ui(driver):

    unique = str(int(time.time()))

    title = "Delete E2E Note " + unique
    description = "This note will be deleted using API"

    api = APIClient() #creates the api tool
    api.login()

    create_response = api.create_note(title, description, "Home") #it creates note using the api in home
    assert create_response.status_code == 200

    note_id = create_response.json()["data"]["id"] #it gives the id for the created above one note

    notes_response = api.get_notes()
    notes = notes_response.json()["data"]

    created_note_found = False

    for note in notes: #it checks whether the note is created or not
        if note["id"] == note_id: 
            created_note_found = True
            break

    assert created_note_found

#to delete the note using api
    delete_response = api.delete_note(note_id)
    assert delete_response.status_code == 200

    after_delete_response = api.get_notes()
    after_delete_notes = after_delete_response.json()["data"] #it checks by using id is it deleted or no to check

    deleted_note_found = False

#if note not found ten it deleted succesfuuly
    for note in after_delete_notes:
        if note["id"] == note_id:
            deleted_note_found = True
            break

    assert deleted_note_found == False

    login_page = LoginPage(driver)
    login_page.login(config["email"], config["password"]) 

    home_page = HomePage(driver)

    driver.refresh()
    time.sleep(3)

    assert home_page.is_note_not_visible(title)