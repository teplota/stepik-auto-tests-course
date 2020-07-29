from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        check_current_url = self.check_current_url()
        assert "/login" in check_current_url, "Wrong login url"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def new_user_registration(self, email, password1, password2):
        assert self.is_element_present(*LoginPageLocators.EMAIL), "Email field is not presented"
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)                              # Ввести емейл
        assert self.is_element_present(*LoginPageLocators.PASSWORD1), "Password field is not presented"
        self.browser.find_element(*LoginPageLocators.PASSWORD1).send_keys(password1)                      # Ввести пароль
        assert self.is_element_present(*LoginPageLocators.PASSWORD2), "Password repeat field is not presented"
        self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password2)                      # Повторить пароль
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()                         # Нажать на кнопку "Зарегистрироваться"

    def existed_user_login(self, email, password):
        assert self.is_element_present(*LoginPageLocators.EMAIL_LOGIN), "Email field is not presented"
        self.browser.find_element(*LoginPageLocators.EMAIL_LOGIN).send_keys(email)                         # Ввести емейл
        assert self.is_element_present(*LoginPageLocators.PASSWORD_LOGIN), "Password field is not presented"
        self.browser.find_element(*LoginPageLocators.PASSWORD_LOGIN).send_keys(password)                   # Ввести пароль
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()                                 # Нажать на кнопку "Войти"

    def should_be_registration_successful(self):                                                           # Успешная регистрация
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_MESSAGE), "Registration message is not presented"
        registration_message = self.element_text(*LoginPageLocators.REGISTRATION_MESSAGE)
        return registration_message

    def should_not_be_registration_successful(self):                                                        # Неуспешная регистрация
        assert self.is_element_present(*LoginPageLocators.ERROR_REGISTRATION_MESSAGE), "Error registration message is not presented"
        error_registration_message = self.element_text(*LoginPageLocators.ERROR_REGISTRATION_MESSAGE)
        return error_registration_message

    def should_be_error_registration_message_below(self):                                                    # Сообщение об ошибке при регистрации
        assert self.is_element_present(*LoginPageLocators.ERROR_REGISTRATION_MESSAGE_BELOW), "Error registration message below is not presented"
        error_registration_message_below = self.element_text(*LoginPageLocators.ERROR_REGISTRATION_MESSAGE_BELOW)
        return error_registration_message_below

    def check_should_be_logout_link(self):                                                                   # Должна быть ссылка "выйти"
        return self.is_element_present(*BasePageLocators.LOGOUT_LINK)

    def check_should_not_be_login_link(self):                                                                # Не должно быть ссылки "войти"
        return self.is_not_element_present(*BasePageLocators.LOGIN_LINK)

    def should_be_login_successful(self):                                                                    # Пользователь дожен быть успешно авторизован
        assert self.is_element_present(*BasePageLocators.WELCOME_MESSAGE), "Welcome message is not presented"
        welcome_message = self.element_text(*BasePageLocators.WELCOME_MESSAGE)
        return welcome_message
