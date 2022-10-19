from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from .locators import PromoNewYearPageLocator
from .locators import BasePageLocators
from .locators import BasketPageLocator



import math


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.maximize_window()
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    #
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*PromoNewYearPageLocator.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_disappeared_element(self):
        assert self.is_disappeared(*PromoNewYearPageLocator.SUCCESS_MESSAGE), \
            "Success message is't disappeared, but should not be"

        #

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_main_page(self):
        self.should_be_root_link()
        link = self.browser.find_element(*BasePageLocators.ROOT_LINK)
        link.click()

    def should_be_root_link(self):
        assert self.is_element_present(*BasePageLocators.ROOT_LINK), "Root link is not presented"

    def search_send_keys(self):
        search_input = self.browser.find_element(*BasePageLocators.SEARCH_INPUT)
        search_input.send_keys("Coders at Work")

    def click_search_button(self):
        search_button = self.browser.find_element(*BasePageLocators.SEARCH_BUTTON)
        search_button.click()

    def go_to_basket_page(self):
        self.should_be_basket_button()
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()
        self.should_be_basket_link()

    def should_be_basket_link(self):
        assert "basket" in self.browser.current_url, "This is not a shopping cart page."

    def should_be_basket_button(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket button is not presented"

    def get_current_link(self):
        print(self.browser.current_url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"