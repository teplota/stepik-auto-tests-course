from .base_page import BasePage
from .locators import RegistrationLocators
from selenium.webdriver.common.by import By
from random import randint

class RegistrationPage(BasePage):
    def enter_email(self):                              # Ввести новый емейл
        self.should_be_email()
        email_new = f'new_email-{randint(1, 10000)}@email.com'
        self.browser.find_element(*RegistrationLocators.EMAIL).send_keys(email_new)

    def enter_password1(self):                          # Ввести пароль
        self.should_be_password1()
        self.browser.find_element(*RegistrationLocators.PASSWORD1).send_keys('veryHardP147')

    def enter_password2(self):                          # Повторить пароль
        self.should_be_password2()
        self.browser.find_element(*RegistrationLocators.PASSWORD2).send_keys('veryHardP147')

    def submit_registration_button(self):               # Нажать на кнопку "Зарегистрироваться"
        self.should_be_registration_button()
        self.browser.find_element(*RegistrationLocators.REGISTRATION_BUTTON).click()

    def should_be_registration_successful(self):        # Успешная регистрация, появление сообщения "Thanks for registering!"
        self.should_be_message_successful()
        registration_message = self.browser.find_element(*RegistrationLocators.REGISTRATION_MESSAGE)
        assert "Thanks for registering!" in registration_message.text, 'Wrong registration message'

    def should_be_email(self):
        assert self.is_element_present(*RegistrationLocators.EMAIL), "Email form is not presented"

    def should_be_password1(self):
        assert self.is_element_present(*RegistrationLocators.PASSWORD1), "Password form is not presented"

    def should_be_password2(self):
        assert self.is_element_present(*RegistrationLocators.PASSWORD2), "Repeat password form is not presented"

    def should_be_registration_button(self):
        assert self.is_element_present(*RegistrationLocators.REGISTRATION_BUTTON), "Registration button is not presented"

    def should_be_message_successful(self):
        assert self.is_element_present(*RegistrationLocators.REGISTRATION_MESSAGE), "Registration message is not presented"

