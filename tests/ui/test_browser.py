import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход в конструктор из ленты заказов")
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
    
        main_page.click_order_feed()
        assert order_feed_page.is_order_feed_displayed()
    
        main_page.click_constructor()
    
        assert main_page.is_constructor_displayed()


@allure.feature("Ингредиенты")
class TestIngredientModal:

    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.click_first_ingredient()

        assert main_page.is_ingredient_modal_displayed()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        main_page.click_first_ingredient()
        assert main_page.is_ingredient_modal_displayed()

        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_closed()


@allure.feature("Конструктор")
class TestIngredientCounter:

    @allure.title("Добавление булочки увеличивает счётчик ингредиента")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)

        counter_after = main_page.add_bun_and_get_counter()

        assert counter_after == "2"


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Успешная авторизация зарегистрированного пользователя")
    def test_login_registered_user(self, driver, registered_user):
        user_data, _ = registered_user

        main_page = MainPage(driver)

        main_page.login(
            user_data["email"],
            user_data["password"]
        )

        assert main_page.is_constructor_displayed()


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Успешное создание заказа авторизованным пользователем")
    def test_create_order(self, driver, registered_user):
        user_data, _ = registered_user

        main_page = MainPage(driver)

        main_page.login(
            user_data["email"],
            user_data["password"]
        )

        main_page.add_first_ingredient_to_constructor()
        main_page.click_order_button()

        assert main_page.is_order_modal_displayed()

        main_page.wait_for_order_loading()

        order_number = main_page.get_order_number()

        assert order_number != ""


@allure.feature("Лента заказов")
class TestOrderFeedCounters:

    @allure.title("Проверка отображения счётчиков заказов")
    def test_order_feed_counters_are_displayed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed()

        total_count = order_feed_page.get_total_orders_count()
        today_count = order_feed_page.get_today_orders_count()

        assert total_count >= 0
        assert today_count >= 0


class TestTotalOrdersCounter:

    @allure.title("Проверка увеличения счётчика заказов после создания заказа")
    def test_total_orders_counter_increases_after_order_creation(
        self, driver, registered_user
    ):
        user_data, _ = registered_user

        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.login(
            user_data["email"],
            user_data["password"]
        )

        main_page.click_order_feed()

        initial_count = order_feed_page.get_total_orders_count()

        main_page.click_constructor()
        main_page.add_first_ingredient_to_constructor()
        main_page.click_order_button()

        assert main_page.is_order_modal_displayed()

        main_page.wait_for_order_loading()
        main_page.close_order_modal()
        assert main_page.wait_for_order_modal_closed()

        main_page.click_order_feed()

        assert order_feed_page.wait_for_total_orders_increase(
            initial_count
        )


class TestTodayOrdersCounter:

    @allure.title("Проверка увеличения счётчика заказов за сегодня")
    def test_today_orders_counter_increases_after_order_creation(
        self, driver, registered_user
    ):
        user_data, _ = registered_user

        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.login(
            user_data["email"],
            user_data["password"]
        )

        main_page.click_order_feed()

        initial_count = order_feed_page.get_today_orders_count()

        main_page.click_constructor()
        main_page.add_first_ingredient_to_constructor()
        main_page.click_order_button()

        assert main_page.is_order_modal_displayed()

        main_page.wait_for_order_loading()
        main_page.close_order_modal()
        assert main_page.wait_for_order_modal_closed()

        main_page.click_order_feed()

        assert order_feed_page.wait_for_today_orders_increase(
            initial_count
        )


class TestOrdersInProgress:

    @allure.title("Проверка появления номера созданного заказа в разделе «В работе»")
    def test_order_number_appears_in_progress(
        self, driver, registered_user
    ):
        user_data, _ = registered_user

        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.login(
            user_data["email"],
            user_data["password"]
        )

        main_page.add_first_ingredient_to_constructor()
        main_page.click_order_button()

        assert main_page.is_constructor_displayed()

        main_page.wait_for_order_loading()
        order_number = main_page.get_order_number()

        assert order_number != ""

        main_page.close_order_modal()
        assert main_page.wait_for_order_modal_closed()

        main_page.click_order_feed()

        assert order_feed_page.wait_for_order_in_progress(
            order_number
        )
