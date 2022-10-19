from .base_page import BasePage
from .locators import BasketPageLocator
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocator.BASKET_NOT_EMPTY_MASSEGE), \
            "Products are presented in the basket, but should not be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocator.BASKET_IS_EMPTY_MASSEGE), \
            "Basket is full, but should not be"
