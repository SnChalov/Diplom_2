import allure
from pages.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Перейти в конструктор")
    def click_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Перейти в ленту заказов")
    def click_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Выбрать первый ингредиент")
    def click_first_ingredient(self):
        self.click_element(MainPageLocators.FIRST_INGREDIENT)

    @allure.step("Проверить отображение модального окна ингредиента")
    def is_ingredient_modal_displayed(self):
        return self.find_element(
            MainPageLocators.INGREDIENT_MODAL
        ).is_displayed()

    @allure.step("Проверить закрытие модального окна ингредиента")
    def is_ingredient_modal_closed(self):
        return self.wait_for_invisibility(
            MainPageLocators.INGREDIENT_MODAL
        )

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_element(
            MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON
        )

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_element(
            MainPageLocators.ORDER_MODAL_CLOSE_BUTTON
        )
        self.wait_for_order_modal_closed()
        self.wait_for_modal_overlay_closed()

    @allure.step("Авторизоваться")
    def login(self, email, password):
        self.click_element(
            MainPageLocators.PERSONAL_ACCOUNT_BUTTON
        )
        self.find_element(
            MainPageLocators.EMAIL_INPUT
        ).send_keys(email)
        self.find_element(
            MainPageLocators.PASSWORD_INPUT
        ).send_keys(password)
        self.click_element(MainPageLocators.LOGIN_BUTTON)
        self.wait_for_modal_overlay_closed()

    @allure.step("Проверить отображение кнопки оформления заказа")
    def is_order_button_displayed(self):
        return self.find_element(
            MainPageLocators.ORDER_BUTTON
        ).is_displayed()

    @allure.step("Добавить первый ингредиент в конструктор")
    def add_first_ingredient_to_constructor(self):
        ingredient = self.find_element(
            MainPageLocators.FIRST_INGREDIENT
        )

        drop_area = self.find_element(
            MainPageLocators.BUN_DROP_AREA
        )

        self.execute_script("""
            const ingredient = arguments[0];
            const dropArea = arguments[1];
            const dataTransfer = new DataTransfer();

            ingredient.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            dropArea.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            dropArea.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            dropArea.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));

            ingredient.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            }));
        """, ingredient, drop_area)

    @allure.step("Получить счётчик первого ингредиента")
    def get_first_ingredient_counter(self):
        ingredient = self.find_element(
            MainPageLocators.FIRST_INGREDIENT
        )

        counter = ingredient.find_element(
            *MainPageLocators.INGREDIENT_COUNTER
        )

        return counter.text

    @allure.step("Добавить булочку и проверить изменение счётчика")
    def add_bun_and_get_counter(self):
        counter_before = self.get_first_ingredient_counter()

        self.add_first_ingredient_to_constructor()

        self.wait_for_condition(
            lambda driver:
            self.get_first_ingredient_counter() != counter_before,
            timeout=10
        )

        return self.get_first_ingredient_counter()

    @allure.step("Нажать кнопку оформления заказа")
    def click_order_button(self):
        self.click_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проверить отображение модального окна заказа")
    def is_order_modal_displayed(self):
        return self.find_element(
            MainPageLocators.ORDER_MODAL
        ).is_displayed()

    @allure.step("Дождаться завершения загрузки заказа")
    def wait_for_order_loading(self):
        return self.wait_for_invisibility(
            MainPageLocators.LOADING_MODAL
        )

    @allure.step("Получить номер созданного заказа")
    def get_order_number(self):
        return self.get_element_text(
            MainPageLocators.ORDER_NUMBER
        ).strip()

    @allure.step("Дождаться закрытия модального окна заказа")
    def wait_for_order_modal_closed(self):
        return self.wait_for_invisibility(
            MainPageLocators.ORDER_MODAL
        )

    @allure.step("Проверить отображение ингредиентов конструктора")
    def is_constructor_displayed(self):
        return self.find_element(
            MainPageLocators.FIRST_INGREDIENT
        ).is_displayed()

    @allure.step("Дождаться закрытия затемняющего слоя")
    def wait_for_modal_overlay_closed(self):
        return self.wait_for_invisibility(
            MainPageLocators.MODAL_OVERLAY
        )

    @allure.step("Проверить отображение конструктора")
    def is_constructor_displayed(self):
        return self.find_element(
            MainPageLocators.FIRST_INGREDIENT
        ).is_displayed()

    @allure.step("Дождаться закрытия всех затемняющих слоёв")
    def wait_for_modal_overlay_closed(self):
        return self.wait_for_all_invisibility(
            MainPageLocators.MODAL_OVERLAY
        )
