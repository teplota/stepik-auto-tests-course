import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

def test_presense_of_add_button(browser):
    """
    Проверка  наличия кнопки добавления в корзину
    1. открыть браузер, перейти на страницу товара
    2. проверить наличие кнопки "добавить в корзину"
    ОР: кнопка присутствует
    """

    # Открыть браузер, перейти по адресу
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # проверить наличие кнопки "добавить в корзину"
    def check_button():
        try:
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#add_to_basket_form button')))
        except TimeoutException:
            return False
        return True
    assert check_button(),  'Кнопка добавления товара отсутствует'
