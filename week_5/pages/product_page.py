from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def add_product_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"                  # Проверяем наличие кнопки добавления товара в корзину
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()                                              # Добавляем товар в корзину

    def product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Product price is not presented"                    # Проверяем наличие цены товара
        product_price = self.element_text(*ProductPageLocators.PRICE)
        return product_price

    def product_title(self):
        assert self.is_element_present(*ProductPageLocators.TITLE), "Product title is not presented"                    # Проверяем наличие названия товара
        product_title = self.element_text(*ProductPageLocators.TITLE)
        return product_title

    def should_be_message_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), "'Basket price' message is not presented"  # Проверяем наличие сообщения со стоимость корзины
        message_product_price = self.element_text(*ProductPageLocators.MESSAGE_PRICE)
        return message_product_price

    def should_be_message_product_title(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_TITLE), "'Product added' message is not presented"  # Проверяем наличие сообщения, что товар добавлен в корзину
        message_product_title = self.element_text(*ProductPageLocators.MESSAGE_TITLE)
        return message_product_title


