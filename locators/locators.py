from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//a[contains(., 'Конструктор')]"
    )
    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//a[contains(., 'Лента Заказов')]"
    )

    FIRST_INGREDIENT = (
        By.XPATH,
        "(//*[contains(@class, 'BurgerIngredient_ingredient')])[1]"
    )

    INGREDIENT_COUNTER = (
        By.XPATH,
        ".//*[contains(@class, 'counter') and @class]"
    )

    INGREDIENT_MODAL = (
        By.XPATH,
        "//*[contains(@class, 'Modal_modal') and not(contains(@class, 'overlay'))]"
    )

    INGREDIENT_MODAL_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "div[class*='Modal_modal']:not([class*='overlay']) button[class*='Modal_modal__close']"
    )

    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Оформить заказ')]"
    )

    BUN_DROP_AREA = (
        By.CSS_SELECTOR,
        "ul[class*='BurgerConstructor_basket__list']"
    )

    PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        "//a[contains(., 'Личный Кабинет')]"
    )

    EMAIL_INPUT = (
        By.XPATH,
        "//input[@type='text' or @type='email']"
    )

    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Войти')]"
    )

    ORDER_MODAL = (
        By.XPATH,
        "//*[contains(@class, 'Modal_modal') and not(contains(@class, 'overlay'))]"
    )

    ORDER_NUMBER = (
        By.XPATH,
        "//*[contains(@class, 'Modal_modal')]//h2"
    )

    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        "div[class*='Modal_modal_overlay']"
    )

    LOADING_MODAL = (
        By.CSS_SELECTOR,
        "img[alt='loading animation']"
    )

    ORDER_MODAL_CLOSE_BUTTON = (
        By.CSS_SELECTOR,
        "div[class*='Modal_modal']:not([class*='overlay']) button[class*='Modal_modal__close']"
    )

class OrderFeedPageLocators:
    ORDER_FEED_TITLE = (
        By.XPATH,
        "//*[contains(text(), 'Лента заказов')]"
    )

    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )

    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )

    ORDERS_IN_PROGRESS = (
        By.XPATH,
        "//*[contains(text(), 'В работе')]"
    )

    ORDERS_IN_PROGRESS_TEXT = (
        By.XPATH,
        "//*[contains(text(), 'В работе')]/.."
    )
