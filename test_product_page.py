"""
1. Проверка добавить товар в корзину и пройти валидацию
2. Запустить сразу несколько тестов, используя @pytest.mark.parametrize. Седьмую ссылку помечать как Пропуск т.к Оштбка

pytest -v --tb=line --language=en test_product_page.py
pytest -v --tb=line --language=en -m need_review
"""
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# Первоз далание на проверку, добавить в корзину
def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()

# Второе задание на проверку добавитьв корзину
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()

# Третие задание из 3 тестов. Проверка отсутствие элемента, (2 тест проходит, 1 и 3 помечаем mark.xfail )
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_dissappeared()

# Четвертое задание вызывать страницу логиеа с людой вкладки
def test_guest_should_see_login_link_on_product_page(browser): # Коректность линк
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):  # Проверка возможности перехода
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()                                    # Гость открывает страницу товара
    page.go_to_basket_page()                       # Переходит в корзину по кнопке в шапке
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()           # Ожидаем, что в корзине нет товаров
    basket_page.should_be_message_empty_basket()   # Ожидаем, что есть текст о том что корзина пуста

class TestUserAddToBasketFromProductPage():
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_guest_cant_see_success_message(self, browser):
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.add_to_basket()
        self.page.should_be_book_name()
        self.page.should_be_book_price()
