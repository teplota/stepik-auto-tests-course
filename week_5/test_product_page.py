from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)                 # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес страницы товара
    page.open()                                       # Открываем страницу
    page.add_product_to_basket()                      # Добавляем товар в корзину
    page.solve_quiz_and_get_code()                    # Считаем результат мат.выражения и вводим ответ
    page.should_be_added_product()                    # Проверяем, что товар добавлен в корзину

