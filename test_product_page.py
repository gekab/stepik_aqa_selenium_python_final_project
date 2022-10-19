import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
import time
import random


def random_string():
    word = ""
    for i in range(5):
        word = word + chr(random.randrange(48, 58)) + chr(random.randrange(65, 91)) + chr(random.randrange(97, 123))
    return word

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        # Добавьте в класс фикстуру setup. В этой функции нужно:
        # открыть страницу регистрации;
        # зарегистрировать нового пользователя;
        # проверить, что пользователь залогинен.
        login_page = LoginPage(browser, link)
        login_page.open()
        email = random_string() + "@fakemail.org"
        password = random_string()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
        # time.sleep(1)

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_button()
        page.add_to_basket_page()
        page.should_be_purchase()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('links', [
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    #              marks=pytest.mark.skip),
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip
# @pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_can_add_product_to_basket(browser, links):
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()
    page.should_be_purchase()
    time.sleep(2)


@pytest.mark.skip
@pytest.mark.parametrize('links', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, links):
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_to_basket_page()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('links', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, links):
    # Открываем страницу товара
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('links', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, links):
    # Открываем страницу товара
    # Добавляем товар в корзину
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    link = links
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_to_basket_page()
    # time.sleep(5)
    page.should_disappeared_element()


# @pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


# @pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)
