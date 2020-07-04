from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_1():
    """
    Перехода в подкатегории товара
    1. открыть браузер, перейти по адресу
    2. выбрать категорию books
    3. выбрать подкатегорию non-fiction
    4. выбрать подгатегорию essential-programming
    ОР: совершен переход в выбранную подкатегорию
    """

    # Предусловия: в интернет-магазине есть категория товаров books и подкатегории non-fiction и essential-programming

    # Адрес сайта:
    link = "http://selenium1py.pythonanywhere.com/ru/"

    try:
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--disable-gpu')
        browser = webdriver.Chrome(options=chrome_opt)
        # говорим WebDriver искать каждый элемент в течение 5 секунд
        browser.implicitly_wait(5)

        # Открыть браузер, перейти по адресу
        browser.get(link)

        # Выбрать категорию Books
        books = browser.find_element(By.XPATH, "//a[text()='Books']").click()

        # Выбрать подкатегорию Non-Fiction
        nonfiction = browser.find_element_by_css_selector(".side_categories a[href='/ru/catalogue/category/books/non-fiction_5/']").click()

        # Выбрать подкатегорию Essential programming
        essentialprogramming = browser.find_element_by_css_selector(".side_categories a[href='/ru/catalogue/category/books/non-fiction/essential-programming_6/']").click()

        # Проверить, что находимся в выбранной категории
        activecategory = browser.find_element_by_css_selector(".breadcrumb .active")

        assert "Essential programming" in activecategory.text

        # Сообщение об успешном выполнении теста
        print("test_1 'Переход в подкатегории товара' passed")

    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_2():
    """
    Добавление первого товара в корзину
    1. открыть страницу товара
    2. зафиксировать название и стоимость товара
    3. нажать кнопку "добавить в корзину"
    ОР: товар добавлен в корзину:
    - появилось сообщение "товар был добавлен в вашу корзину"
    - появилось сообщение "стоимость корзины теперь составляет *стоимость товара*
    - стоимость товаров в корзине увеличилась на величину стоимости товара
    """

    # Предусловия: на складе должна присутствовать книга "The shellcoder's handbook"

    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"

    try:
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--disable-gpu')
        browser = webdriver.Chrome(options=chrome_opt)
        # говорим WebDriver искать каждый элемент в течение 5 секунд
        browser.implicitly_wait(5)

        # Открыть браузер, перейти по адресу страницы товара
        browser.get(link)

        # Зафиксировать название и стоимость выбранного товара.
        title = browser.find_element_by_css_selector(".product_page h1")
        book_title = title.text

        price = browser.find_element_by_css_selector(".product_page .price_color")
        book_price = price.text

       # Под выбранным товаром нажать кнопку "Добавить в корзину"
        button_add = browser.find_element_by_css_selector(".btn-add-to-basket").click()

        # Товар добавлен в корзину:
        # Появилось сообщение: "название товара" был добавлен в вашу корзину
        message_add = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alertinner"))
        )
        x = book_title + " был добавлен в вашу корзину."
        assert x in message_add.text
        #assert "The shellcoder's handbook был добавлен в вашу корзину." in message_add.text

        # Появилось сообщение: Стоимость корзины теперь составляет "стоимость товара"
        message_price = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Стоимость корзины теперь составляет')]"))
        )
        y = "Стоимость корзины теперь составляет " + book_price
        assert y in message_price.text

        # Стоимость товаров в корзине увеличилась на величину стоимости добавленного товара, отображается: Всего в корзине: "стоимость товара" £
        price_basket = browser.find_element_by_css_selector(".basket-mini")
        z = "Всего в корзине: " + book_price
        assert z in price_basket.text

        # Сообщение об успешном выполнении теста
        print("test_2 'Добавление первого товара в корзину' passed")


    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_3(email_registered, password_registered):
    """
    Авторизация зарегистрированного пользователя
    1. открыть браузер, перейти по адресу магазина
    2. перейти на страницу "войти или зарегистрироваться"
    3. ввести адрес электронной почты
    4. ввести пароль
    5. нажать "войти"
    ОР: пользователь авторизован, отображается сообщение "рады видеть вас снова"
    """
    # Предусловия: в тесте используются зарегистрированные ранее адрес электронной почты и пароль

    # Адрес сайта:
    link = "http://selenium1py.pythonanywhere.com/ru/"

    try:
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--disable-gpu')
        browser = webdriver.Chrome(options=chrome_opt)
        # Искать каждый элемент в течение 5 секунд
        browser.implicitly_wait(5)

        # Открыть браузер, перейти по адресу
        browser.get(link)

        # С главной страницы перейти на страницу "войти или зарегистрироваться"
        login_link = browser.find_element_by_id("login_link")
        login_link.click()

        # В блоке "Войти" в поле "Адрес электронной почты" ввести зарегистрированный адрес электронной почты
        email = browser.find_element_by_id("id_login-username")
        email.send_keys(email_registered)

        # В поле "Пароль" ввести пароль от данного аккаунта
        password = browser.find_element_by_id("id_login-password")
        password.send_keys(password_registered)

        # Нажать кнопку "Войти"
        login = browser.find_element_by_name("login_submit")
        login.click()

        # Проверять в течение 5 секунд, пока не появится сообщение об успешной авторизации
        message = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alertinner"))
        )
        assert "Рады видеть вас снова" in message.text

        # Сообщение об успешном выполнении теста
        print("test_3 'Авторизация зарегистрированного пользователя' passed")

    finally:
        # Закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    test_1()
    test_2()
    test_3('dohapa4146@lefaqr5.com', 'Selenium111') # Зарегистрированные ранее адрес электронной почты и пароль

 # не забываем оставить пустую строку в конце файла
