import requests
import json

from environs import Env

env = Env()
env.read_env()


class TrelloManager:
    TOKEN = 'ATTAf239568721bcc9e1f8287eff0f668e12937b217eef5e0c024746a04391b27f1f3B86744C'
    KEY = '0a0dd946a3a0b525997c63e2fe3060f1'

    def __init__(self, username):
        self.username = username

    @staticmethod
    def get_list_id_widt_name(list_data, name):
        try:
            return [data.get('id') for data in list_data if data.get('name') == name][0]
        except IndexError as e:
            print(e)

    @staticmethod
    def base_headers():
        return {
            "Accept": "application/json"
        }

    def credentials(self):
        return {
            'key': self.KEY,
            "token": self.TOKEN
        }

    def get_member_id(self):
        url = f"https://api.trello.com/1/members/{self.username}"

        response = requests.request(
            "GET",
            url,
            headers=self.base_headers(),
            params=self.credentials()
        )
        if response.status_code == 200:
            return json.loads(response.text).get("id")

    def get_boards(self):
        url = f"https://api.trello.com/1/members/{self.username}/boards"

        response = requests.request(
            "GET",
            url,
            headers=self.base_headers(),
            params=self.credentials()
        )

        if response.status_code == 200:
            return json.loads(response.text)

    def get_lists_on_a_board(self, board_id):
        url = url = f"https://api.trello.com/1/boards/{board_id}/lists"

        response = requests.request(
            "GET",
            url,
            headers=self.base_headers(),
            params=self.credentials()
        )

        if response.status_code == 200:
            return json.loads(response.text)

    def get_cards_on_a_list(self, list_id):
        url = f"https://api.trello.com/1/lists/{list_id}/cards"

        response = requests.request(
            "GET",
            url,
            headers=self.base_headers(),
            params=self.credentials()
        )

        if response.status_code == 200:
            return json.loads(response.text)

    def get_board_id_with_name(self, name):
        try:
            return [board.get('id') for board in self.get_boards() if board.get('name') == name][0]
        except IndexError as e:
            print(e)

    def get_board_members(self, board_id):
        url = f"https://api.trello.com/1/boards/{board_id}/memberships"

        response = requests.request(
            "GET",
            url,
            headers=self.base_headers(),
            params=self.credentials()
        )

        if response.status_code == 200:
            return json.loads(response.text)