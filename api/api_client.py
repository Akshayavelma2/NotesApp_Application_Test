#this api client interact with all apis 

import requests
from config.environment import config

class APIClient:

    def __init__(self):
        self.base_url = config["api_url"]
        self.token = None
#login method
#self means instance of class
    def login(self):
        url = f"{self.base_url}/users/login"

        payload = {
            "email": config["email"],
            "password": config["password"]
        }

        response = requests.post(url, json=payload)

        assert response.status_code == 200

        self.token = response.json()["data"]["token"]

        return response
#it gives notes
    def get_notes(self):
        url = f"{self.base_url}/notes"

        headers = {
            "x-auth-token": self.token
        }

        return requests.get(url, headers=headers)
#creates notes
    def create_note(self, title, description, category="Home"):
        url = f"{self.base_url}/notes"

        headers = {
            "x-auth-token": self.token
        }

        payload = {
            "title": title,
            "description": description,
            "category": category
        }

        return requests.post(url, json=payload, headers=headers)
#delete the notes by id
    def delete_note(self, note_id):
        url = f"{self.base_url}/notes/{note_id}"

        headers = {
            "x-auth-token": self.token
        }

        return requests.delete(url, headers=headers)