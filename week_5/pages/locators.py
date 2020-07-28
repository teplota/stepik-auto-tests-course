from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")
    WELCOME_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    #BASKET_LINK = (By.LINK_TEXT, "View basket")
    BASKET_LINK = (By.XPATH, "//span/a[contains(@href,'basket')]")
    #//span/a[contains(@href,'basket')]
    #.basket - mini.btn - default
    CHECKOUT_LINK = (By.XPATH, "//p/a[contains(@href,'checkout')]")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, ".content #content_inner")


class CheckoutPageLocators():
    FIRST_NAME = (By.ID, 'id_first_name')
    LAST_NAME = (By.ID, 'id_last_name')
    FIRST_LINE_ADDRESS = (By.ID, 'id_line1')
    CITY = (By.ID, 'id_line4')
    POSTCODE = (By.ID, 'id_postcode')
    COUNTRY = (By.ID, 'id_country')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, ".form-group .btn")
    PAYMENT_CONTINUE_BUTTON = (By.CSS_SELECTOR, ".btn")
    ADDRESS_FORM = (By.XPATH, "//address")
    ORDER_CONTENTS = (By.CSS_SELECTOR, ".basket-items h3 a")
    ORDER_TOTAL = (By.CSS_SELECTOR, ".total .price_color")
    ORDER_CONFIRMATION = (By.CSS_SELECTOR, ".lead")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "#place-order")


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