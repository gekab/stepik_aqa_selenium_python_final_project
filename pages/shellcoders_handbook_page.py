from .base_page import BasePage
from .locators import PromoNewYearPageLocator
from selenium.webdriver.common.by import By

class ShellcodersHandbookPage(BasePage):
    def add_to_basket_page(self):
        basket_button = self.browser.find_element(*PromoNewYearPageLocator.ADD_BUTTON)
        basket_button.click()

    def should_be_purchase(self):
        # self.should_be_shellcoder_text()
        self.should_be_9_99_price()

    def should_be_basket_button(self):
        assert self.is_element_present(*PromoNewYearPageLocator.ADD_BUTTON), "Basket button is not presented"

    def should_be_shellcoder_text(self):
        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили
        act_result = self.browser.find_element(*PromoNewYearPageLocator.NAME2_BOOK).text
        exp_result = self.browser.find_element(*PromoNewYearPageLocator.NAME1_BOOK).text
        assert exp_result in act_result, "Should be The shellcoder's handbook"

    def should_be_9_99_price(self):
        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара
        act_result = self.browser.find_element(*PromoNewYearPageLocator.PRICE_TEXT_MESSAGE).text
        exp_result = self.browser.find_element(*PromoNewYearPageLocator.PRICE_TEXT).get_attribute('innerHTML')
        assert exp_result[:-9] in act_result, f"Price {exp_result[:-9]} is not presented {act_result}"
