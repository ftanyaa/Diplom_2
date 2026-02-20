import allure
from helpers.order_helper import OrderHelper
from data.payloads import INVALID_INGREDIENTS
from data.messages import UNAUTHORIZED


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_authorized(self, auth_token):
        ingredients = OrderHelper.get_valid_ingredients()

        response = OrderHelper.create_order(
            token=auth_token,
            ingredients=ingredients
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_no_auth(self):
        ingredients = OrderHelper.get_valid_ingredients()

        response = OrderHelper.create_order(
            ingredients=ingredients
        )

        assert response.status_code == 200

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, auth_token):
        ingredients = OrderHelper.get_valid_ingredients()

        response = OrderHelper.create_order(
            token=auth_token,
            ingredients=ingredients
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, auth_token):
        response = OrderHelper.create_order(
            token=auth_token,
            ingredients=[]
        )

        assert response.status_code == 400

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash(self, auth_token):
        response = OrderHelper.create_order(
            token=auth_token,
            ingredients=INVALID_INGREDIENTS
        )

        assert response.status_code == 500

