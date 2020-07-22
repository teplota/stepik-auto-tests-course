from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()                                                                                             # Переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()                                                                                             # Переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()                                                                                   # Выполняем проверку, что осуществлен переход на страницу логина

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, empty_basket_message):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()                                                                                                         # Гость открывает главную страницу
    page.go_to_basket_page()                                                                                            # Переходит в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url)
    assert basket_page.should_not_be_items_in_basket, "There is some items in basket, but it should not be"             # Ожидаем, что в корзине нет товаров
    assert empty_basket_message == basket_page.should_be_message_empty_basket(), "'Basket price' message  is wrong"     # Ожидаем, что есть текст о том что корзина пуста
