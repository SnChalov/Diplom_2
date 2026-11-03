from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.locators import OrderFeedPageLocators


class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_order_feed_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                OrderFeedPageLocators.ORDER_FEED_TITLE
            )
        ).is_displayed()

    def get_total_orders_count(self):
        counter = self.wait.until(
            EC.visibility_of_element_located(
                OrderFeedPageLocators.TOTAL_ORDERS_COUNTER
            )
        )
        return int(counter.text)

    def get_today_orders_count(self):
        counter = self.wait.until(
            EC.visibility_of_element_located(
                OrderFeedPageLocators.TODAY_ORDERS_COUNTER
            )
        )
        return int(counter.text)

    def get_orders_in_progress_text(self):
        element = self.wait.until(
            EC.visibility_of_element_located(
                OrderFeedPageLocators.ORDERS_IN_PROGRESS
            )
        )
        return element.find_element(By.XPATH, "..").text

    def is_order_number_in_progress(self, order_number):
        orders_text = self.get_orders_in_progress_text()
        return str(order_number).zfill(6) in orders_text.split()
