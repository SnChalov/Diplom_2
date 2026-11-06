import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from data.urls import REGISTER_URL, USER_URL
from helpers.user_data import generate_user_data


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.maximize_window()
    browser.get("https://qa-stellarburgers.education-services.ru/")

    WebDriverWait(browser, 20).until(
        lambda current_browser: current_browser.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    WebDriverWait(browser, 20).until(
        lambda current_browser: not any(
            overlay.is_displayed()
            for overlay in current_browser.find_elements(
                By.CSS_SELECTOR,
                "div.Modal_modal_overlay__x2ZCr"
            )
        )
    )

    yield browser

    browser.quit()


@pytest.fixture
def user_data():
    return generate_user_data()


@pytest.fixture
def registered_user(user_data):
    response = requests.post(
        REGISTER_URL,
        json=user_data,
        timeout=10,
    )

    assert response.status_code == 200, response.text

    response_data = response.json()

    yield user_data, response_data

    access_token = response_data.get("accessToken")

    if access_token:
        requests.delete(
            USER_URL,
            headers={"Authorization": access_token},
            timeout=10,
        )
