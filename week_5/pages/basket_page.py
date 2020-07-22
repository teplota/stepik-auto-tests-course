from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        return self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Empty basket message is not presented"
        empty_basket_message = self.element_text(*BasketPageLocators.EMPTY_BASKET_MESSAGE)
        return empty_basket_message


