from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.ID, "login_link")
    LOGIN_FORM = (By.NAME, "login_submit")
    REGISTER_FORM = (By.NAME, "registration_submit")


class PromoNewYearPageLocator():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_TEXT_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    NAME1_BOOK = (By.CSS_SELECTOR, ".product_main > h1")
    NAME2_BOOK = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner :nth-child(1)")