import pytest
from pages.main_page import MainPage
from pages.shellcoders_handbook_page import ShellcodersHandbookPage
import time


@pytest.mark.parametrize('links', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.skip),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_can_add_product_to_basket(browser, links):
    link = links
    page = ShellcodersHandbookPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()
    page.should_be_purchase()
    time.sleep(5)
