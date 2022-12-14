from .base_page import BasePage
from .locators import PromoNewYearPageLocator
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_to_basket_page(self):
        basket_button = self.browser.find_element(*PromoNewYearPageLocator.ADD_BUTTON)
        basket_button.click()

    def should_be_purchase(self):
        self.should_be_shellcoder_text()
        self.should_be_9_99_price()

    def should_be_shellcoder_text(self):
        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        # который вы действительно добавили
        act_result = self.browser.find_element(*PromoNewYearPageLocator.NAME2_BOOK).text
        exp_result = self.browser.find_element(*PromoNewYearPageLocator.NAME1_BOOK).text
        assert exp_result == act_result, f"The title of book {exp_result} does not match the title of book {act_result}"

    def should_be_9_99_price(self):
        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
        act_result = self.browser.find_element(*PromoNewYearPageLocator.PRICE_TEXT_MESSAGE).text
        exp_result = self.browser.find_element(*PromoNewYearPageLocator.PRICE_TEXT).get_attribute('innerHTML')
        assert exp_result[:5] == act_result[:5], f"Price {exp_result[:5]} is not equal to price {act_result}"

    def add_to_basket(self):
        self.should_be_add_to_basket_link()
        add_to_basket_button = self.browser.find_element(*PromoNewYearPageLocator.ADD_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_link(self):
        assert self.is_element_present(*PromoNewYearPageLocator.ADD_BUTTON), \
            "Add to Basket button is not presented"

