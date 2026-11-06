import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти видимый элемент")
    def find_element(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Нажать на элемент")
    def click_element(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Получить текст элемента")
    def get_element_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Дождаться исчезновения элемента")
    def wait_for_invisibility(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Дождаться выполнения условия")
    def wait_for_condition(self, condition, timeout=10):
        return WebDriverWait(
            self.driver, timeout
        ).until(condition)

    @allure.step("Выполнить JavaScript")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Дождаться исчезновения всех элементов")
    def wait_for_all_invisibility(self, locator):
        return self.wait.until(
            lambda driver: not any(
                element.is_displayed()
                for element in driver.find_elements(*locator)
            )
        )