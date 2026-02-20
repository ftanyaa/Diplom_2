import pytest
from helpers.user_helper import UserHelper
from data.payloads import user_payload


@pytest.fixture
def create_new_user():
    payload = user_payload()
    response = UserHelper.create_user(payload)
    return payload, response.json()


@pytest.fixture
def auth_token(create_new_user):
    payload, response = create_new_user
    return response["accessToken"]
