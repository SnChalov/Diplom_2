import allure
import requests
from data.urls import LOGIN_URL


@allure.feature("Авторизация пользователя")
class TestLoginUser:

    @allure.title("Успешная авторизация зарегистрированного пользователя")
    @allure.description("Проверка входа с корректными email и паролем.")
    def test_login_existing_user_returns_success(self, registered_user):
        user_data, _ = registered_user

        response = requests.post(
            LOGIN_URL,
            json={
                "email": user_data["email"],
                "password": user_data["password"],
            },
            timeout=10,
        )

        assert response.status_code == 200
        response_data = response.json()

        assert response_data["success"] is True
        assert response_data["user"]["email"] == user_data["email"]
        assert response_data["user"]["name"] == user_data["name"]
        assert response_data["accessToken"]
        assert response_data["refreshToken"]

    @allure.title("Ошибка авторизации с неверными данными")
    @allure.description("Проверка входа с несуществующим email и неверным паролем.")
    def test_login_with_wrong_credentials_returns_error(self, user_data):
        response = requests.post(
            LOGIN_URL,
            json={
                "email": user_data["email"],
                "password": "WrongPassword123",
            },
            timeout=10,
        )

        assert response.status_code == 401
        response_data = response.json()

        assert response_data["success"] is False
        assert response_data["message"] == "email or password are incorrect"
