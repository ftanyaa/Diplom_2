import allure
from helpers.user_helper import UserHelper
from data.payloads import user_payload, login_payload
from data.messages import LOGIN_ERROR


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self):
        payload = user_payload()
        UserHelper.create_user(payload)

        login_data = login_payload(payload["email"], payload["password"])
        response = UserHelper.login_user(login_data)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Вход с неверным логином и паролем")
    def test_login_invalid_credentials(self):
        login_data = login_payload("wrong@mail.com", "wrongpass")

        response = UserHelper.login_user(login_data)

        assert response.status_code == 401
        assert response.json()["message"] == LOGIN_ERROR
