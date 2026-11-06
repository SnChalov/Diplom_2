import allure
from pages.base_page import BasePage
from locators.locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step("Проверить отображение ленты заказов")
    def is_order_feed_displayed(self):
        return self.find_element(
            OrderFeedPageLocators.ORDER_FEED_TITLE
        ).is_displayed()

    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        return int(
            self.get_element_text(
                OrderFeedPageLocators.TOTAL_ORDERS_COUNTER
            )
        )

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        return int(
            self.get_element_text(
                OrderFeedPageLocators.TODAY_ORDERS_COUNTER
            )
        )

    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress_text(self):
        return self.get_element_text(
            OrderFeedPageLocators.ORDERS_IN_PROGRESS_TEXT
        )

    @allure.step("Проверить наличие номера заказа в работе")
    def is_order_number_in_progress(self, order_number):
        orders_text = self.get_orders_in_progress_text()
        return str(order_number).zfill(6) in orders_text.split()

    @allure.step("Дождаться увеличения общего количества заказов")
    def wait_for_total_orders_increase(self, initial_count):
        return self.wait_for_condition(
            lambda driver: self.get_total_orders_count() > initial_count,
            timeout=30
        )

    @allure.step("Дождаться увеличения количества заказов за сегодня")
    def wait_for_today_orders_increase(self, initial_count):
        return self.wait_for_condition(
            lambda driver: self.get_today_orders_count() > initial_count,
            timeout=30
        )

    @allure.step("Дождаться появления номера заказа в работе")
    def wait_for_order_in_progress(self, order_number):
        return self.wait_for_condition(
            lambda driver: self.is_order_number_in_progress(order_number),
            timeout=30
        )
