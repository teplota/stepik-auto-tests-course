import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from random import randint
from datetime import datetime

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='Chrome')
    parser.addoption('--language', action='store', default='en-gb')

@pytest.fixture(scope="function")
def browser(request):
    user_browser = request.config.getoption('browser')
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if user_browser == "Chrome":
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
    else:
        print('Browser is not supported')
    yield browser
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def registration_text(request):
    user_language = request.config.getoption('language')
    registration_text = {
        'en-gb': '×\nThanks for registering!',
        'en': '×\nThanks for registering!',
        'ru': '×\nСпасибо за регистрацию!'
    }
    return registration_text[user_language]

@pytest.fixture(scope="function")
def error_registration_text(request):
    user_language = request.config.getoption('language')
    error_registration_text = {
        'en-gb': 'Oops! We found some errors - please check the error messages below and try again',
        'en': 'Oops! We found some errors - please check the error messages below and try again',
        'ru': 'Опаньки! Мы нашли какие-то ошибки - пожалуйста, проверьте сообщения об ошибках ниже и попробуйте еще раз'
    }
    return error_registration_text[user_language]

@pytest.fixture(scope="function")
def error_registration_message_below_email_already_exist(request):
    user_language = request.config.getoption('language')
    error_registration_message_below_email_already_exist = {
        'en-gb': "A user with that email address already exists",
        'en': "A user with that email address already exists",
        'ru': 'Пользователь с таким адресом электронной почты уже зарегистрирован.'
    }
    return error_registration_message_below_email_already_exist[user_language]

@pytest.fixture(scope="function")
def error_registration_message_below_password_did_not_match(request):
    user_language = request.config.getoption('language')
    error_registration_message_below_password_did_not_match = {
        'en-gb': "The two password fields didn't match.",
        'en': "The two password fields didn't match.",
        'ru': 'Два поля с паролями не совпадают.'
    }
    return error_registration_message_below_password_did_not_match[user_language]

@pytest.fixture(scope="function")
def error_registration_message_below_password_is_too_short(request):
    user_language = request.config.getoption('language')
    error_registration_message_below_password_is_too_short = {
        'en-gb': "This password is too short. It must contain at least 9 characters.",
        'en': "This password is too short. It must contain at least 9 characters.",
        'ru': 'Введённый пароль слишком короткий. Он должен содержать как минимум 9 символов.'
    }
    return error_registration_message_below_password_is_too_short[user_language]

@pytest.fixture(scope="function")
def error_registration_message_below_password_is_too_common(request):
    user_language = request.config.getoption('language')
    error_registration_message_below_password_is_too_common = {
        'en-gb': "This password is too common.",
        'en': "This password is too common.",
        'ru': 'Введённый пароль слишком широко распространён.'
    }
    return error_registration_message_below_password_is_too_common[user_language]

@pytest.fixture(scope="function")
def welcome_massage_when_user_login(request):
    user_language = request.config.getoption('language')
    welcome_massage_when_user_login = {
        'en-gb': "×\nWelcome back",
        'en': "×\nWelcome back",
        'ru': '×\nРады видеть вас снова'
    }
    return welcome_massage_when_user_login[user_language]

@pytest.fixture(scope="function")
def empty_basket_message(request):
    user_language = request.config.getoption('language')
    welcome_massage_when_user_login = {
        'en-gb': "Your basket is empty. Continue shopping",
        'en': "Your basket is empty. Continue shopping",
        'ru': 'Ваша корзина пуста Продолжить покупки'
    }
    return welcome_massage_when_user_login[user_language]

@pytest.fixture(scope="function")
def email_already_exist():
    email_already_exist = 'dohapa41467@lefaqr5.com'  # Зарегистрированный ранее пользователь, пароль veryHardP147
    return email_already_exist

@pytest.fixture(scope="function")
def email_invalid():
    email_invalid = '111@111'
    return email_invalid

@pytest.fixture(scope="function")
def email():
    email = f'test_new_email-{randint(1, 10000)}@email.com'
    return email

@pytest.fixture(scope="function")
def password_valid():
    password_valid = 'veryHardP147'                 # Валидный пароль, такой же у зарегистрированного пользователя
    return password_valid

@pytest.fixture(scope="function")
def password_short():
    password_short = 'ads'
    return password_short

@pytest.fixture(scope="function")
def password_common():
    password_common = 'qwerty123'
    return password_common

@pytest.fixture(scope="function")
def link_login():
    link_login = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    return link_login

@pytest.fixture(scope="function")
def link_main():
    link_main = 'http://selenium1py.pythonanywhere.com/'
    return link_main

@pytest.fixture(scope="function")
def link_product():
    link_product = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/'
    return link_product

@pytest.fixture(scope="function")
def test_first_name():
    test_first_name = "Ivan"
    return test_first_name

@pytest.fixture(scope="function")
def test_last_name():
    test_last_name = "Ivanov"
    return test_last_name

@pytest.fixture(scope="function")
def test_first_lane_address():
    test_first_lane_address = "Prospekt Prospektov 1"
    return test_first_lane_address

@pytest.fixture(scope="function")
def test_city():
    test_city = "Big-City"
    return test_city

@pytest.fixture(scope="function")
def postcode():
    postcode = "199999"
    return postcode

@pytest.fixture(scope="function")
def country():
    country = "Russian Federation"
    return country

@pytest.fixture(scope="function")
def product_title():
    product_title = "The shellcoder's handbook"
    return product_title

@pytest.fixture(scope="function")
def product_price():
    product_price = "£9.99"
    return product_price

@pytest.fixture(scope="function")
def order_confirmation_message(request):
    user_language = request.config.getoption('language')
    order_confirmation_message = {
        'en-gb': "Your order has been placed and a confirmation email has been sent - your order number is",
        'en': "Your order has been placed and a confirmation email has been sent - your order number is",
        'ru': 'Ваш заказ был размещен и выслано сообщение с подтверждением - номер вашего заказа'
    }
    return order_confirmation_message[user_language]


