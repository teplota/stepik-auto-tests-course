from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def product_title(self):
        assert self.is_element_present(*ProductPageLocators.TITLE), "Product title is not presented"                    # Проверяем наличие названия товара
        product_title = self.element_text(*ProductPageLocators.TITLE)
        return product_title

    def product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Product price is not presented"                    # Проверяем наличие цены товара
        product_price = self.element_text(*ProductPageLocators.PRICE)
        return product_price

    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"                  # Проверяем наличие кнопки добавления товара в корзину
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()                                              # Добавляем товар в корзину

    def should_be_added_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_TITLE), "'Product added' message is not presented"  # Проверяем наличие сообщения, что товар добавлен в корзину
        product_title = self.product_title()
        self.should_be_correct_message_title(product_title)                                                             # Проверяем, что сообщение верно
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), "'Basket price' message is not presented"   # Проверяем наличие сообщения со стоимость корзины
        product_price = self.product_price()
        self.should_be_correct_message_price(product_price)                                                             # Проверяем, что цена верна


    def should_be_correct_message_title(self, product_title):
        message_product_added = self.element_text(*ProductPageLocators.MESSAGE_TITLE)
        assert product_title == message_product_added, "'Product added' message  is wrong"

    def should_be_correct_message_price(self, product_price):
        message_product_price = self.element_text(*ProductPageLocators.MESSAGE_PRICE)
        assert product_price == message_product_price, "'Basket price' message  is wrong"
