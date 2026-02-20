import allure
from helpers.user_helper import UserHelper
from data.payloads import user_payload
from data.messages import USER_EXISTS, REQUIRED_FIELDS_ERROR


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создать уникального пользователя")
    def test_create_unique_user(self):
        payload = user_payload()
        response = UserHelper.create_user(payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_existing_user(self):
        payload = user_payload()

        UserHelper.create_user(payload)
        response = UserHelper.create_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == USER_EXISTS

    @allure.title("Создать пользователя без обязательного поля")
    def test_create_user_without_required_field(self):
        payload = user_payload()
        payload.pop("email")

        response = UserHelper.create_user(payload)

        assert response.status_code == 403
        assert response.json()["message"] == REQUIRED_FIELDS_ERROR
