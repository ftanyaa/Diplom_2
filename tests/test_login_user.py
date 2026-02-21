import allure
from helpers.user_helper import UserHelper
from data.payloads import VALID_USER, LOGIN_VALID
from data.messages import LOGIN_ERROR


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self):
        import random
        email = f"test_user_{random.randint(10000, 99999)}@mail.com"
        password = VALID_USER["password"]
        user_payload = VALID_USER.copy()
        user_payload["email"] = email

        with allure.step("Создание пользователя для логина"):
            UserHelper.create_user(user_payload)

        login_data = {"email": email, "password": password}
        with allure.step("Вход под существующим пользователем"):
            response = UserHelper.login_user(login_data)

        assert response.status_code == 200
        assert response.json()["success"] is True


    @allure.title("Вход с неверным логином и паролем")
    def test_login_invalid_credentials(self):
        invalid_login = {"email": "wrong@mail.com", "password": "wrongpass"}

        with allure.step("Попытка входа с неверными учетными данными"):
            response = UserHelper.login_user(invalid_login)

        assert response.status_code == 401
        assert response.json()["message"] == LOGIN_ERROR

