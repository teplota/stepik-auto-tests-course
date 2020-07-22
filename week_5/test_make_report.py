import pytest
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from random import randint


def test_guest_can_register_unique_email(browser, password_valid, registration_text):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    email = f'new_email-{randint(1, 10000)}@email.com'
    password1 = password2 = password_valid
    login_page.new_user_registration(email, password1, password2)
    assert login_page.check_should_be_logout_link(),"Logout link is not presented"
    assert login_page.check_should_not_be_login_link(), "Login link is presented, but should not be"
    assert registration_text == login_page.should_be_registration_successful(), 'Wrong registration message'