import requests
from data.urls import BASE_URL, CREATE_USER, LOGIN_USER


class UserHelper:

    @staticmethod
    def create_user(payload):
        return requests.post(f"{BASE_URL}{CREATE_USER}", json=payload)

    @staticmethod
    def login_user(payload):
        return requests.post(f"{BASE_URL}{LOGIN_USER}", json=payload)
