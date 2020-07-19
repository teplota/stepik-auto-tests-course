from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from random import randint

def test_guest_can_register_unique_email(browser, password_valid, registration_text):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                               # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                                  # Открываем страницу
    page.go_to_login_page()                                      # Переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    email = f'new_email-{randint(1, 10000)}@email.com'
    password1 = password2 = password_valid
    login_page.new_user_registration(email, password1, password2)
    registration_message = login_page.should_be_registration_successful()
    assert registration_text in registration_message, 'Wrong registration message'

def test_guest_can_not_register_email_already_exist(browser, email_already_exist, password_valid, error_registration_text, error_registration_message_below_email_already_exist):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                               # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                                  # Открываем страницу
    page.go_to_login_page()                                      # Переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    email = email_already_exist
    password1 = password2 = password_valid
    login_page.new_user_registration(email, password1, password2)
    error_registration_message = login_page.should_not_be_registration_successful()
    assert error_registration_text in error_registration_message, 'Wrong error registration message'
    error_registration_message_below = login_page.should_be_error_registration_message_below()
    assert error_registration_message_below_email_already_exist in error_registration_message_below, 'Wrong error registration message below'

def test_guest_can_not_register_password_repeat_did_not_match(browser, password_valid, error_registration_text, error_registration_message_below_password_did_not_match):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                               # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                                  # Открываем страницу
    page.go_to_login_page()                                      # Переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    email = f'new_email-{randint(1, 10000)}@email.com'
    password1 = password_valid
    password2 = f'{password_valid}111'
    login_page.new_user_registration(email, password1, password2)
    error_registration_message = login_page.should_not_be_registration_successful()
    assert error_registration_text in error_registration_message, 'Wrong error registration message'
    error_registration_message_below = login_page.should_be_error_registration_message_below()
    assert error_registration_message_below_password_did_not_match in error_registration_message_below, 'Wrong error registration message below'


