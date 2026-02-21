import pytest
import random
from helpers.user_helper import UserHelper
from data.payloads import VALID_USER


def generate_unique_email():
    return f"test_user_{random.randint(10000, 99999)}@mail.com"


@pytest.fixture
def create_new_user():
    payload = VALID_USER.copy()
    payload["email"] = generate_unique_email()
    response = UserHelper.create_user(payload)
    return payload, response.json()


@pytest.fixture
def auth_token(create_new_user):
    payload, response = create_new_user
    return response.get("accessToken")
