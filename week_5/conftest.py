import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='Chrome')
    parser.addoption('--language', action='store', default='en-gb')

@pytest.fixture(scope="function")
def browser(request):
    user_browser = request.config.getoption('browser')
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if user_browser == "Chrome":
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
    else:
        print('Browser is not supported')
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def registration_text(request):
    user_language = request.config.getoption('language')
    registration_text = {
        'en-gb': 'Thanks for registering!',
        'de': 'Danke für Ihre Registrierung!',
        'es': 'Gracias por registrarse!',
        'fr': 'Merci de vous être enregistré !',
        'ru': 'Спасибо за регистрацию!'
    }
    return registration_text[user_language]

@pytest.fixture(scope="function")
def error_registration_text(request):
    user_language = request.config.getoption('language')
    error_registration_text = {
        'en-gb': 'Oops! We found some errors - please check the error messages below and try again',
        'de': 'Ups! Es sind Fehler aufgetreten - bitte korrigieren Sie die untenstehenden Fehler und versuchen Sie es erneut',
        'es': 'Oops! Encontramos algunos errores - Por favor, comprueba el mensaje de error siguiente e inténtalo de nuevo',
        'fr': "Oups ! Nous avons trouvé des erreurs - veuillez vérifier les messages d'erreur ci-dessous et réessayer",
        'ru': 'Опаньки! Мы нашли какие-то ошибки - пожалуйста, проверьте сообщения об ошибках ниже и попробуйте еще раз'
    }
    return error_registration_text[user_language]

@pytest.fixture(scope="function")
def error_registration_message_below_email_already_exist(request):
    user_language = request.config.getoption('language')
    error_registration_message_below_email_already_exist = {
        'en-gb': "A user with that email address already exists",
        'ru': 'Два поля с паролями не совпадают.'
    }
    return error_registration_message_below_email_already_exist[user_language]

@pytest.fixture(scope="function")
def error_registration_message_below_password_did_not_match(request):
    user_language = request.config.getoption('language')
    error_registration_message_below_password_did_not_match = {
        'en-gb': "The two password fields didn't match.",
        'ru': 'Два поля с паролями не совпадают.'
    }
    return error_registration_message_below_password_did_not_match[user_language]

@pytest.fixture(scope="function")
def email_already_exist():
    email_already_exist = 'dohapa4146@lefaqr5.com' #Зарегистрированный ранее пользователь
    return email_already_exist

@pytest.fixture(scope="function")
def password_already_exist():
    password_already_exist = 'Selenium111'          #Пароль зарегистрированого ранее пользователя
    return password_already_exist

@pytest.fixture(scope="function")
def email_invalid():
    email_invalid = '111'
    return email_invalid

@pytest.fixture(scope="function")
def password_valid():
    password_valid = 'veryHardP147'
    return password_valid

@pytest.fixture(scope="function")
def password_invalid():
    password_invalid = '111'
    return password_invalid



