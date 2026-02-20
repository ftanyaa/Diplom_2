import random
import string


def generate_email():
    return f"test_{random.randint(10000, 99999)}@mail.com"


def generate_password():
    return "Password123"


def generate_name():
    return "TestUser"


def user_payload():
    return {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name()
    }


def login_payload(email, password):
    return {
        "email": email,
        "password": password
    }


VALID_INGREDIENTS = [
    "60d3463f7034a000269f45e9",
    "60d3463f7034a000269f45e7"
]

INVALID_INGREDIENTS = [
    "invalid_hash_123"
]
