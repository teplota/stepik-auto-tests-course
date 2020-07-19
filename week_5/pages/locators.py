from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_LOGIN = (By.ID, 'id_login-username')
    PASSWORD_LOGIN = (By.ID, 'id_login-password')
    LOGIN_BUTTON = (By.NAME, 'login_submit')
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD1 = (By.ID, 'id_registration-password1')
    PASSWORD2 = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')
    REGISTRATION_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')
    ERROR_REGISTRATION_MESSAGE = (By.CSS_SELECTOR, '#register_form .alert-danger')
    ERROR_REGISTRATION_MESSAGE_BELOW = (By.CSS_SELECTOR, '.has-error .error-block')

class ProductPageLocators():
    TITLE = (By.CSS_SELECTOR, ".product_page h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    MESSAGE_TITLE = (By.CSS_SELECTOR, "#messages .alert-success strong")
    MESSAGE_PRICE = (By.CSS_SELECTOR, "#messages .alert-info strong")
