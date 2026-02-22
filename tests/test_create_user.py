import allure
import random
from helpers.user_helper import UserHelper
from data.payloads import VALID_USER
from data.messages import USER_EXISTS, REQUIRED_FIELDS_ERROR


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user(self):
        payload = VALID_USER.copy()
        payload["email"] = f"test_user_{random.randint(10000, 99999)}@mail.com"

        with allure.step("Создание уникального пользователя"):
            response = UserHelper.create_user(payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_existing_user(self):
        payload = VALID_USER.copy()
        payload["email"] = f"test_user_{random.randint(10000, 99999)}@mail.com"

        with allure.step("Создание первого пользователя"):
            UserHelper.create_user(payload)

        with allure.step("Попытка создать того же пользователя снова"):
            response = UserHelper.create_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == USER_EXISTS

    @allure.title("Создать пользователя без обязательного поля")
    def test_create_user_without_required_field(self):
        payload = VALID_USER.copy()
        payload["email"] = f"test_user_{random.randint(10000, 99999)}@mail.com"
        payload.pop("email")

        with allure.step("Попытка создать пользователя без email"):
            response = UserHelper.create_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == REQUIRED_FIELDS_ERROR
