import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint

class Locators:
    email = (By.ID, 'id_registration-email')
    password1 = (By.ID, 'id_registration-password1')
    password2 = (By.ID, 'id_registration-password2')
    button_registration = (By.NAME, 'registration_submit')
    message = (By.CSS_SELECTOR, '#messages .alert-success')


def test_new_user_registration(browser):
    """
    Проверка  регистрации нового пользователя
    1. открыть браузер, перейти на страницу регистрации
    2. ввести логин
    3. ввести пароль
    4. повторить пароль
    5. нажать на кнопку "зарегистрироваться"
    ОР: успешная регистрация, появление сообщения "Спасибо за регистрацию!"
    """
    #Сгенерировать случайный емейл
    email_new = f'new_email-{randint(1, 10000)}@email.com'

    # Открыть браузер, перейти на страницу регистрации
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    browser.get(link)

    # ввести логин
    browser.find_element(*Locators.email).send_keys(email_new)

    # ввести пароль
    browser.find_element(*Locators.password1).send_keys('veryHardP147')

    # повторить пароль
    browser.find_element(*Locators.password2).send_keys('veryHardP147')

    # нажать на кнопку "зарегистрироваться"
    browser.find_element(*Locators.button_registration).click()

    #успешная регистрация, появление сообщения "Спасибо за регистрацию!"
    registration_message = browser.find_element(*Locators.message)
    assert "Спасибо за регистрацию!" in registration_message.text, 'Wrong registration message!'
