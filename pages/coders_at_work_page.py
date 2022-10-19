from .base_page import BasePage
from .locators import CodersAtWorkLocators


class CodersAtWorkPage(BasePage):
    def add_to_basket(self):
        self.should_be_add_to_basket_link()
        add_to_basket_button = self.browser.find_element(*CodersAtWorkLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_link(self):
        assert self.is_element_present(*CodersAtWorkLocators.ADD_TO_BASKET_BUTTON), \
            "Add to Basket button is not presented"