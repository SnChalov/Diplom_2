import allure
import requests
from data.urls import REGISTER_URL


@allure.feature("Регистрация пользователя")
class TestCreateUser:

    @allure.title("Успешная регистрация нового пользователя")
    @allure.description("Проверка регистрации с уникальными email, паролем и именем.")
    def test_create_unique_user_returns_success(self, registered_user):
        user_data, response_data = registered_user

        assert response_data["success"] is True
        assert response_data["user"]["email"] == user_data["email"]
        assert response_data["user"]["name"] == user_data["name"]
        assert response_data["accessToken"]
        assert response_data["refreshToken"]

    @allure.title("Ошибка при регистрации уже существующего пользователя")
    def test_create_existing_user_returns_error(self, registered_user):
        user_data, _ = registered_user

        response = requests.post(
            REGISTER_URL,
            json=user_data,
            timeout=10,
        )

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @allure.title("Ошибка при регистрации без обязательного поля")
    def test_create_user_without_required_field_returns_error(self, user_data):
        incomplete_data = {
            "email": user_data["email"],
            "password": user_data["password"],
        }

        response = requests.post(
            REGISTER_URL,
            json=incomplete_data,
            timeout=10,
        )

        assert response.status_code == 403
        assert response.json()["success"] is False
