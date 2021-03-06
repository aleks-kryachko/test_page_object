"""
pytest -v --tb=line --language=en test_main_page.py

"""
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):  # Переход на страницу Зарегистрироваться
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

def test_guest_should_see_login_link(browser):  # Проверяем ошибку при неправильной страницы
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# добавим отрицательные проверки
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()                        # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()            # Ожидаем, что в корзине нет товаров
    basket_page.should_be_message_empty_basket()    # Ожидаем, что есть текст о том что корзина пуста
