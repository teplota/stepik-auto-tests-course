from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_title()                            # Проверяем название товара
        self.should_be_price()                            # Проверяем цену товара
        self.should_be_add_button()                       # Добавляем кнопку добавления товара в корзину
        self.click_add_button()                           # Добавляем товар в корзину

    def should_be_added_product(self):
        self.should_be_message_product_added_to_basket()  # Проверяем сообщение, что товар добавлен в корзину
        self.should_be_correct_message_title()
        self.should_be_message_basket_price()             # Проверяем сообщение со стоимость корзины
        self.should_be_correct_message_price()

    def should_be_title(self):
        assert self.is_element_present(*ProductPageLocators.TITLE), "Product title is not presented"

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Product price is not presented"

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def click_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def should_be_message_product_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_TITLE), "'Product added' message  is not presented"

    def should_be_message_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_PRICE), "'Basket price' message  is not presented"

    def should_be_correct_message_title(self):
        product_title = self.element_text(*ProductPageLocators.TITLE)
        message_product_added = self.element_text(*ProductPageLocators.MESSAGE_TITLE)
        assert product_title in message_product_added, "'Product added' message  is wrong"

    def should_be_correct_message_price(self):
        product_price = self.element_text(*ProductPageLocators.PRICE)
        message_product_price = self.element_text(*ProductPageLocators.MESSAGE_PRICE)
        assert product_price in message_product_price, "'Basket price' message  is wrong"
