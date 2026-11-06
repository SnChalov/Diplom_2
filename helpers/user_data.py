import uuid


def generate_user_data():
    return {
        "email": f"test_{uuid.uuid4().hex[:10]}@example.com",
        "password": "TestPassword123",
        "name": f"TestUser{uuid.uuid4().hex[:6]}"
    }
    