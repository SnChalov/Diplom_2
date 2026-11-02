from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_constructor(self):
        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.CONSTRUCTOR_BUTTON
            )
        ).click()

    def click_order_feed(self):
        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.ORDER_FEED_BUTTON
            )
        ).click()

    def click_first_ingredient(self):
        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.FIRST_INGREDIENT
            )
        ).click()

    def is_ingredient_modal_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.INGREDIENT_MODAL
            )
        ).is_displayed()

    def close_order_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.ORDER_MODAL_CLOSE_BUTTON
            )
        ).click()

    def login(self, email, password):
        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.PERSONAL_ACCOUNT_BUTTON
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.EMAIL_INPUT
            )
        ).send_keys(email)

        self.driver.find_element(
            *MainPageLocators.PASSWORD_INPUT
        ).send_keys(password)

        self.driver.find_element(
            *MainPageLocators.LOGIN_BUTTON
        ).click()
    
    def add_first_ingredient_to_constructor(self):
        ingredient = self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.FIRST_INGREDIENT
            )
        )

        drop_area = self.wait.until(
            EC.visibility_of_element_located(
                MainPageLocators.BUN_DROP_AREA
            )
        )

        self.driver.execute_script("""
            const ingredient = arguments[0];
            const dropArea = arguments[1];
            const dataTransfer = new DataTransfer();

            ingredient.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true,
                dataTransfer: dataTransfer
            }));

            dropArea.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true,
                dataTransfer: dataTransfer
            }));

            dropArea.dispatchEvent(new DragEvent('dragover', {
                bubbles: true,
                dataTransfer: dataTransfer
            }));

            dropArea.dispatchEvent(new DragEvent('drop', {
                bubbles: true,
                dataTransfer: dataTransfer
            }));

            ingredient.dispatchEvent(new DragEvent('dragend', {
                bubbles: true,
                dataTransfer: dataTransfer
            }));
        """, ingredient, drop_area)

    def click_order_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.ORDER_BUTTON
            )
        ).click()
    
    def close_ingredient_modal(self):
        self.wait.until(
            EC.element_to_be_clickable(
                MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON
            )
        ).click()
        