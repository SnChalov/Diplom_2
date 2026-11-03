import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from locators.locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход в конструктор")
    def test_constructor_button(self, driver):
        main_page = MainPage(driver)

        main_page.click_constructor()

        assert driver.current_url == (
            "https://qa-stellarburgers.education-services.ru/"
        )

    @allure.title("Переход в ленту заказов")
    def test_order_feed_button(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed()

        assert driver.current_url.endswith("/feed")
        assert order_feed_page.is_order_feed_displayed()


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

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(
                MainPageLocators.INGREDIENT_MODAL
            )
        )


@allure.feature("Конструктор")
class TestIngredientCounter:




    @allure.title("Добавление булочки увеличивает счётчик ингредиента")
    def test_ingredient_counter_increases(self, driver):
        ingredient = driver.find_element(
            *MainPageLocators.FIRST_INGREDIENT
        )
    
        counter = ingredient.find_element(
            By.XPATH,
            ".//*[contains(@class, 'counter')][1]"
        )
    
        counter_before = counter.text
    
        drop_area = driver.find_element(
            *MainPageLocators.BUN_DROP_AREA
        )
    
        driver.execute_script("""
            const ingredient = arguments[0];
            const dropArea = arguments[1];
    
            const dataTransfer = new DataTransfer();
    
            ingredient.dispatchEvent(
                new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                })
            );
    
            dropArea.dispatchEvent(
                new DragEvent('dragenter', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                })
            );
    
            dropArea.dispatchEvent(
                new DragEvent('dragover', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                })
            );
    
            dropArea.dispatchEvent(
                new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                })
            );
    
            ingredient.dispatchEvent(
                new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                })
            );
        """, ingredient, drop_area)
    
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(
                *MainPageLocators.FIRST_INGREDIENT
            ).find_element(
                By.XPATH,
                ".//*[contains(@class, 'counter')][1]"
            ).text != counter_before
        )
    
        counter_after = driver.find_element(
            *MainPageLocators.FIRST_INGREDIENT
        ).find_element(
            By.XPATH,
            ".//*[contains(@class, 'counter')][1]"
        ).text
    
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

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                MainPageLocators.ORDER_BUTTON
            )
        )

        assert driver.find_element(
            *MainPageLocators.ORDER_BUTTON
        ).is_displayed()

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

        order_modal = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                MainPageLocators.ORDER_MODAL
            )
        )

        assert order_modal.is_displayed()

        order_number = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(
                MainPageLocators.ORDER_NUMBER
            )
        )

        assert order_number.text.strip() != ""

class TestOrderFeedCounters:

    @allure.title("Проверка отображения счётчиков заказов")
    def test_order_feed_counters_are_displayed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.click_order_feed()

        WebDriverWait(driver, 20).until(
            lambda driver: "Выполнено за все время:" in
            driver.find_element(By.TAG_NAME, "body").text
        )

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
        
        WebDriverWait(driver, 10).until(
            lambda driver: all(
                not overlay.is_displayed()
                for overlay in driver.find_elements(
                    *MainPageLocators.MODAL_OVERLAY
                )
            )
        )
        
        main_page.click_order_feed()

        WebDriverWait(driver, 20).until(
            lambda driver: "Выполнено за все время:" in
            driver.find_element(By.TAG_NAME, "body").text
        )

        initial_count = order_feed_page.get_total_orders_count()

        main_page.click_constructor()
        main_page.add_first_ingredient_to_constructor()
        main_page.click_order_button()

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                MainPageLocators.ORDER_MODAL
            )
        )

        WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located(
                MainPageLocators.LOADING_MODAL
            )
        )

        main_page.close_order_modal()
        
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(
                MainPageLocators.ORDER_MODAL
            )
        )
        
        main_page.click_order_feed()

        WebDriverWait(driver, 30).until(
            lambda driver:
            order_feed_page.get_total_orders_count() > initial_count
        )

        final_count = order_feed_page.get_total_orders_count()

        assert final_count > initial_count

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

        WebDriverWait(driver, 10).until(
            lambda driver: all(
                not overlay.is_displayed()
                for overlay in driver.find_elements(
                    *MainPageLocators.MODAL_OVERLAY
                )
            )
        )

        main_page.click_order_feed()

        WebDriverWait(driver, 20).until(
            lambda driver: "Выполнено за сегодня:" in
            driver.find_element(By.TAG_NAME, "body").text
        )

        initial_count = order_feed_page.get_today_orders_count()

        main_page.click_constructor()
        main_page.add_first_ingredient_to_constructor()
        main_page.click_order_button()

        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                MainPageLocators.ORDER_MODAL
            )
        )

        WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located(
                MainPageLocators.LOADING_MODAL
            )
        )

        main_page.close_order_modal()

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(
                MainPageLocators.ORDER_MODAL
            )
        )

        main_page.click_order_feed()

        WebDriverWait(driver, 30).until(
            lambda driver:
            order_feed_page.get_today_orders_count() > initial_count
        )

        final_count = order_feed_page.get_today_orders_count()

        assert final_count > initial_count

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
    
        WebDriverWait(driver, 10).until(
            lambda driver: all(
                not overlay.is_displayed()
                for overlay in driver.find_elements(
                    *MainPageLocators.MODAL_OVERLAY
                )
            )
        )
    
        main_page.add_first_ingredient_to_constructor()
        main_page.click_order_button()
    
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                MainPageLocators.ORDER_MODAL
            )
        )
    
        WebDriverWait(driver, 30).until(
            EC.invisibility_of_element_located(
                MainPageLocators.LOADING_MODAL
            )
        )
    
        order_number = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(
                *MainPageLocators.ORDER_NUMBER
            ).text.strip()
        )
    
        main_page.close_order_modal()
    
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located(
                MainPageLocators.ORDER_MODAL
            )
        )
    
        main_page.click_order_feed()
    
        WebDriverWait(driver, 30).until(
            lambda driver:
            order_feed_page.is_order_number_in_progress(order_number)
        )
    
        assert order_feed_page.is_order_number_in_progress(order_number)
