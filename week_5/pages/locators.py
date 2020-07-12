from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    TITLE = (By.CSS_SELECTOR, ".product_page h1")
    PRICE = (By.CSS_SELECTOR, ".product_page .price_color")
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    MESSAGE_TITLE = (By.CSS_SELECTOR, "#messages .alert-success")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages .alert-info")

class RegistrationLocators():
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD1 = (By.ID, 'id_registration-password1')
    PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')
    REGISTRATION_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')

