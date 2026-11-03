import allure
import requests
from data.ingredients import (
    BUN_ID,
    SAUCE_ID,
    INVALID_INGREDIENT_ID,
)
from data.urls import LOGIN_URL, ORDERS_URL


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Авторизованный пользователь может создать заказ")
    def test_authorized_user_can_create_order(self, registered_user):
        user_data, _ = registered_user

        login_response = requests.post(
            LOGIN_URL,
            json={
                "email": user_data["email"],
                "password": user_data["password"],
            },
            timeout=10,
        )
        assert login_response.status_code == 200

        access_token = login_response.json()["accessToken"]

        response = requests.post(
            ORDERS_URL,
            headers={"Authorization": access_token},
            json={"ingredients": [BUN_ID, SAUCE_ID]},
            timeout=10,
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]["_id"]

    @allure.title("Неавторизованный пользователь может создать заказ")
    def test_unauthorized_user_can_create_order_with_ingredients(self):
        response = requests.post(
            ORDERS_URL,
            json={"ingredients": [BUN_ID, SAUCE_ID]},
            timeout=10,
        )

        assert response.status_code == 200

        response_data = response.json()
        assert response_data["success"] is True
        assert response_data["order"]["number"]

    @allure.title("Нельзя создать заказ без ингредиентов")
    def test_create_order_without_ingredients_returns_error(self):
        response = requests.post(
            ORDERS_URL,
            json={"ingredients": []},
            timeout=10,
        )

        assert response.status_code == 400
        assert response.json()["success"] is False

    @allure.title("Ошибка при создании заказа с неверным ингредиентом")
    def test_create_order_with_invalid_ingredient_returns_error(self):
        response = requests.post(
            ORDERS_URL,
            json={"ingredients": [INVALID_INGREDIENT_ID]},
            timeout=10,
        )

        assert response.status_code == 500
