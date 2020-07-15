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
