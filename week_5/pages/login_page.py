from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def enter_email(self, email):  # Ввести емейл
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN), "Email field is not presented"
        self.browser.find_element(*LoginPageLocators.EMAIL_LOGIN).send_keys(email)

    def enter_password(self, password):  # Ввести пароль
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN), "Password field is not presented"
        self.browser.find_element(*LoginPageLocators.PASSWORD_LOGIN).send_keys(password)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        check_current_url = self.check_current_url()
        assert "/login" in check_current_url, "Wrong login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"


    def submit_login_button(self):   # Нажать на кнопку "Войти"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def new_user_registration(self, email, password1, password2):
        self.enter_registration_email(email)  # Ввести логин
        self.enter_registration_password1(password1)  # Ввести пароль
        self.enter_registration_password2(password2)  # Повторить пароль
        self.submit_registration_button()  # Нажать на кнопку "Зарегистрироваться"

    def existed_user_login(self, email, password):
        self.enter_email(email)                                # Ввести емейл
        self.enter_password(password)                          # Ввести пароль
        self.submit_login_button()                             # Нажать на кнопку "Войти"

    def enter_registration_email(self, email):                              # Ввести емейл
        assert self.is_element_present(*LoginPageLocators.EMAIL), "Email field is not presented"
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)

    def enter_registration_password1(self, password1):                          # Ввести пароль
        assert self.is_element_present(*LoginPageLocators.PASSWORD1), "Password field is not presented"
        self.browser.find_element(*LoginPageLocators.PASSWORD1).send_keys(password1)

    def enter_registration_password2(self, password2):                          # Повторить пароль
        self.is_element_present(*LoginPageLocators.PASSWORD2), "Password repeat field is not presented"
        self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password2)

    def submit_registration_button(self):               # Нажать на кнопку "Зарегистрироваться"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    def should_be_registration_successful(self):        # Успешная регистрация, появление сообщения с благодарностью за регистрацию
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_MESSAGE), "Registration message is not presented"
        registration_message = self.element_text(*LoginPageLocators.REGISTRATION_MESSAGE)
        return registration_message

    def should_not_be_registration_successful(self):        # Неуспешная регистрация, появление сообщения об ошибке
        assert self.is_element_present(*LoginPageLocators.ERROR_REGISTRATION_MESSAGE), "Error registration message is not presented"
        error_registration_message = self.element_text(*LoginPageLocators.ERROR_REGISTRATION_MESSAGE)
        return error_registration_message

    def should_be_error_registration_message_below(self):
        assert self.is_element_present(*LoginPageLocators.ERROR_REGISTRATION_MESSAGE_BELOW), "Error registration message below is not presented"
        error_registration_message_below = self.element_text(*LoginPageLocators.ERROR_REGISTRATION_MESSAGE_BELOW)
        return error_registration_message_below

    def check_should_be_logout_link(self):
        return self.is_element_present(*BasePageLocators.LOGOUT_LINK)

    def check_should_not_be_login_link(self):
        return self.is_not_element_present(*BasePageLocators.LOGIN_LINK)

    def should_be_login_successful(self):
        assert self.is_element_present(*BasePageLocators.WELCOME_MESSAGE), "Welcome message is not presented"
        welcome_message = self.element_text(*BasePageLocators.WELCOME_MESSAGE)
        return welcome_message






