from .pages.registration_page import RegistrationPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage



def test_guest_can_register_unique_email(browser, registration_text):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                               # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                                  # Открываем страницу
    page.go_to_login_page()                                      # Переходим на страницу логина
    registration_page = RegistrationPage(browser, browser.current_url)
    registration_message = registration_page.new_user_registration()
    assert registration_text in registration_message.text, 'Wrong registration message'
