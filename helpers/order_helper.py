import requests
from data.urls import BASE_URL, CREATE_ORDER, GET_INGREDIENTS


class OrderHelper:
    @staticmethod
    def get_ingredients():
        response = requests.get(f"{BASE_URL}{GET_INGREDIENTS}")
        return response.json()["data"]

    @staticmethod
    def get_valid_ingredients():
        ingredients = OrderHelper.get_ingredients()
        return [ingredients[0]["_id"], ingredients[1]["_id"]]


    @staticmethod
    def create_order(token=None, ingredients=None):
        headers = {}
        if token:
            headers["Authorization"] = token

        data = {"ingredients": ingredients} if ingredients is not None else {}

        return requests.post(
            f"{BASE_URL}{CREATE_ORDER}",
            json=data,
            headers=headers
        )
