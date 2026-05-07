import requests
from config.environment import config
from api.api_client import APIClient

#tis ave negative test cses
def get_auth_headers():

    api = APIClient()
    api.login()

    return {
        "x-auth-token": api.token
    }

#invalid password
def test_api_login_invalid_password():

    url = f'{config["api_url"]}/users/login'

    payload = {
        "email": config["email"],
        "password": "wrong_password"
    }

    response = requests.post(url, json=payload)

    assert response.status_code in [400, 401]

#invalid email
def test_api_login_invalid_email():

    url = f'{config["api_url"]}/users/login'

    payload = {
        "email": "wrongemail@gmail.com",
        "password": "wrongpassword"
    }

    response = requests.post(url, json=payload)

    assert response.status_code in [400, 401]

#creating node without title
def test_create_note_without_title():

    payload = {
        "description": "Missing title",
        "category": "Home"
    }

    response = requests.post(
        f'{config["api_url"]}/notes',
        json=payload,
        headers=get_auth_headers()
    )

    assert response.status_code in [400, 422]

#it creates note witout title & description
def test_create_note_empty_payload():

    response = requests.post(
        f'{config["api_url"]}/notes',
        json={},
        headers=get_auth_headers()
    )

    assert response.status_code in [400, 422]

#fails when no token
def test_create_note_without_token():

    payload = {
        "title": "Unauthorized Note",
        "description": "Should Fail",
        "category": "Home"
    }

    response = requests.post(
        f'{config["api_url"]}/notes',
        json=payload
    )

    assert response.status_code in [401, 403]
