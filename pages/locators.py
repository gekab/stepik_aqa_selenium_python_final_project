from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    ROOT_LINK = (By.CSS_SELECTOR, ".col-sm-7")
    BASKET_LINK = (By.CLASS_NAME, "btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

#     test
    SEARCH_INPUT = (By.ID, "id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.ID, "login_link")
    LOGIN_FORM = (By.NAME, "login_submit")
    REGISTER_FORM = (By.NAME, "registration_submit")
    EMAIL_INPUT = (By.ID, "id_registration-email")
    PASS_INPUT1 = (By.ID, "id_registration-password1")
    PASS_INPUT2 = (By.ID, "id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")



class PromoNewYearPageLocator():
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_TEXT_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    NAME1_BOOK = (By.CSS_SELECTOR, ".product_main > h1")
    NAME2_BOOK = (By.CSS_SELECTOR, ".alert:nth-child(1) div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")


class BasketPageLocator():
    BASKET_NOT_EMPTY_MASSEGE = (By.XPATH, "//h2[contains(text(),'Items to buy now')]")
    BASKET_IS_EMPTY_MASSEGE = (By.XPATH, "//p[contains(text(),'Your basket is empty.')]")
