import pytest
import random
import requests
from helpers.user_helper import UserHelper
from data.payloads import VALID_USER
from data.urls import BASE_URL


def generate_unique_email():
    return f"test_user_{random.randint(10000, 99999)}@mail.com"


@pytest.fixture
def create_new_user():
    payload = VALID_USER.copy()
    payload["email"] = generate_unique_email()

    response = UserHelper.create_user(payload)
    data = response.json()

    yield payload, data

    # Очистка пользователя после теста
    if "accessToken" in data:
        requests.delete(
            f"{BASE_URL}/api/auth/user",
            headers={"Authorization": data["accessToken"]}
        )


@pytest.fixture
def auth_token(create_new_user):
    payload, response = create_new_user
    return response.get("accessToken")
