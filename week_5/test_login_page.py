import pytest
from .pages.base_page import BasePage
from .pages.login_page import LoginPage


def test_guest_can_register_unique_email(browser, email, password_valid, registration_text):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    password1 = password2 = password_valid
    login_page.new_user_registration(email, password1, password2)
    assert login_page.check_should_be_logout_link(),"Logout link is not presented"
    assert login_page.check_should_not_be_login_link(), "Login link is presented, but should not be"
    assert registration_text == login_page.should_be_registration_successful(), 'Wrong registration message'

@pytest.mark.need_review_custom_scenarios
def test_guest_can_not_register_email_already_exist(browser, email_already_exist, password_valid, error_registration_text, error_registration_message_below_email_already_exist):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    email = email_already_exist
    password1 = password2 = password_valid
    login_page.new_user_registration(email, password1, password2)
    error_registration_message = login_page.should_not_be_registration_successful()
    assert error_registration_text == error_registration_message, 'Wrong error registration message'
    assert error_registration_message_below_email_already_exist == login_page.should_be_error_registration_message_below(), 'Wrong error registration message below'

@pytest.mark.need_review_custom_scenarios
def test_guest_can_not_register_email_invalid(browser, email_invalid, password_valid, error_registration_text):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    email = email_invalid
    password1 = password2 = password_valid
    login_page.new_user_registration(email, password1, password2)
    error_registration_message = login_page.should_not_be_registration_successful()
    assert error_registration_text == error_registration_message, 'Wrong error registration message'

@pytest.mark.need_review_custom_scenarios
def test_guest_can_not_register_password_repeat_did_not_match(browser, email, password_valid, error_registration_text, error_registration_message_below_password_did_not_match):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    password1 = password_valid
    password2 = f'{password_valid}111'
    login_page.new_user_registration(email, password1, password2)
    error_registration_message = login_page.should_not_be_registration_successful()
    assert error_registration_text == error_registration_message, 'Wrong error registration message'
    assert error_registration_message_below_password_did_not_match == login_page.should_be_error_registration_message_below(), 'Wrong error registration message below'

@pytest.mark.need_review_custom_scenarios
def test_guest_can_not_register_password_is_too_short(browser, email, password_short, error_registration_text, error_registration_message_below_password_is_too_short):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    password1 = password2 = password_short
    login_page.new_user_registration(email, password1, password2)
    error_registration_message = login_page.should_not_be_registration_successful()
    assert error_registration_text == error_registration_message, 'Wrong error registration message'
    assert error_registration_message_below_password_is_too_short == login_page.should_be_error_registration_message_below(), 'Wrong error registration message below'

@pytest.mark.need_review_custom_scenarios
def test_guest_can_not_register_password_is_too_common(browser, email, password_common, error_registration_text, error_registration_message_below_password_is_too_common):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    password1 = password2 = password_common
    login_page.new_user_registration(email, password1, password2)
    error_registration_message = login_page.should_not_be_registration_successful()
    assert error_registration_text == error_registration_message, 'Wrong error registration message'
    assert error_registration_message_below_password_is_too_common == login_page.should_be_error_registration_message_below(), 'Wrong error registration message below'

@pytest.mark.need_review_custom_scenarios
def test_user_can_login(browser, email_already_exist, password_valid, welcome_massage_when_user_login):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    email = email_already_exist
    password = password_valid
    login_page.existed_user_login(email, password)
    assert login_page.check_should_be_logout_link(), "Logout link is not presented"
    assert login_page.check_should_not_be_login_link(), "Login link is presented, but should not be"
    assert welcome_massage_when_user_login == login_page.should_be_login_successful(), 'Wrong welcome message'


