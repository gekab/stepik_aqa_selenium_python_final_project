from pages.main_page import MainPage
from pages.shellcoders_handbook_page import ShellcodersHandbookPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ShellcodersHandbookPage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.add_to_basket_page()
    page.solve_quiz_and_get_code()
    page.should_be_purchase()
    time.sleep(1)

