from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])

def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()                                                                                                         # Открываем страницу
    page.add_product_to_basket()                                                                                        # Добавляем товар в корзину
    page.solve_quiz_and_get_code()                                                                                      # Считаем результат мат.выражения и вводим ответ
    assert page.product_title() == page.should_be_message_product_title(), "'Product added' message  is wrong"
    assert page.product_price() == page.should_be_message_product_price(), "'Basket price' message  is wrong"


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, empty_basket_message):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()                                                                                                         # Гость открывает страницу товара
    page.go_to_basket_page()                                                                                            # Переходит в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.should_not_be_items_in_basket, "There is some items in basket, but it should not be"             # Ожидаем, что в корзине нет товаров
    assert empty_basket_message == basket_page.should_be_message_empty_basket(), "'Basket price' message  is wrong"     # Ожидаем, что есть текст о том что корзина пуста

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, email, password_valid):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        password1 = password2 = password_valid
        page.new_user_registration(email, password1, password2)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        assert page.product_title() == page.should_be_message_product_title(), "'Product added' message  is wrong"
        assert page.product_price() == page.should_be_message_product_price(), "'Basket price' message  is wrong"