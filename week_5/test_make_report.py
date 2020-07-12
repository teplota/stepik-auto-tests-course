from .pages.registration_page import RegistrationPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_register_unique_email(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                               # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                                  # Открываем страницу
    page.go_to_login_page()                                      # Переходим на страницу логина
    registration_page = RegistrationPage(browser, browser.current_url)
    registration_page.enter_email()                              # Ввести логин
    registration_page.enter_password1()                          # Ввести пароль
    registration_page.enter_password2()                          # Повторить пароль
    registration_page.submit_registration_button()               # Нажать на кнопку "Зарегистрироваться"
    registration_page.should_be_registration_successful()        # Успешная регистрация, появление сообщения "Спасибо за регистрацию!"
