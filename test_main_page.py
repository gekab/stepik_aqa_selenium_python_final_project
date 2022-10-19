import pytest
from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.main_page
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    # Гость открывает главную страницу
    # Переходит в корзину по кнопке в шапке сайта
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    link = "http://selenium1py.pythonanywhere.com/"
    basket_page = BasketPage(browser, link)
    basket_page.open()
    basket_page.go_to_basket_page()
    time.sleep(5)

    # тест когда товар добавлен в корзину
    # basket_page.search_send_keys()
    # basket_page.click_search_button()
    # browser.find_element(By.XPATH, '//button[text()="Add to basket"]').click()
    # browser.find_element(By.XPATH, '//a[text()="View basket"]').click()
    #

    basket_page.should_not_be_products()
    basket_page.should_be_empty_basket_message()
    time.sleep(5)

@pytest.mark.product_page
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Гость открывает страницу товара
    # Переходит в корзину по кнопке в шапке
    # Ожидаем, что в корзине нет товаров
    # Ожидаем, что есть текст о том что корзина пуста
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products()
    basket_page.should_be_empty_basket_message()
    time.sleep(2)


@pytest.mark.login_guest
class TestLoginFromMainPage:
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.should_be_login_link()