import uuid
import pytest
import requests
from data.urls import REGISTER_URL, USER_URL


@pytest.fixture
def user_data():
    unique_id = uuid.uuid4().hex

    return {
        "email": f"test_{unique_id}@example.com",
        "password": "TestPassword123",
        "name": f"TestUser_{unique_id}",
    }


@pytest.fixture
def registered_user(user_data):
    response = requests.post(
        REGISTER_URL,
        json=user_data,
        timeout=10,
    )

    assert response.status_code == 200, response.text

    response_data = response.json()
    access_token = response_data["accessToken"]

    yield user_data, response_data

    requests.delete(
        USER_URL,
        headers={"Authorization": access_token},
        timeout=10,
    )
