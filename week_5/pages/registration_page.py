from .base_page import BasePage
from .locators import RegistrationLocators
from selenium.webdriver.common.by import By
from random import randint

class RegistrationPage(BasePage):

    def new_user_registration(self):
        self.enter_email()  # Ввести логин
        self.enter_password1()  # Ввести пароль
        self.enter_password2()  # Повторить пароль
        self.submit_registration_button()  # Нажать на кнопку "Зарегистрироваться"
        registration_message = self.should_be_registration_successful()  # Успешная регистрация, появление сообщения "Спасибо за регистрацию!"
        return registration_message

    def enter_email(self):                              # Ввести новый емейл
        assert self.is_element_present(*RegistrationLocators.EMAIL), "Email form is not presented"
        email_new = f'new_email-{randint(1, 10000)}@email.com'
        self.browser.find_element(*RegistrationLocators.EMAIL).send_keys(email_new)

    def enter_password1(self):                          # Ввести пароль
        assert self.is_element_present(*RegistrationLocators.PASSWORD1), "Password form is not presented"
        self.browser.find_element(*RegistrationLocators.PASSWORD1).send_keys('veryHardP147')

    def enter_password2(self):                          # Повторить пароль
        assert self.is_element_present(*RegistrationLocators.PASSWORD2), "Repeat password form is not presented"
        self.browser.find_element(*RegistrationLocators.PASSWORD2).send_keys('veryHardP147')

    def submit_registration_button(self):               # Нажать на кнопку "Зарегистрироваться"
        assert self.is_element_present(*RegistrationLocators.REGISTRATION_BUTTON), "Registration button is not presented"
        self.browser.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

    def should_be_registration_successful(self):        # Успешная регистрация, появление сообщения "Thanks for registering!"
        assert self.is_element_present(*RegistrationLocators.REGISTRATION_MESSAGE), "Registration message is not presented"
        registration_message = self.browser.find_element(*RegistrationLocators.REGISTRATION_MESSAGE)
        return registration_message
