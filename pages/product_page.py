import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_book_name()
        self.should_be_book_price()

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Кнопки добавить нет"
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):   # Проходим валидацию считаем контрольную сумму
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_BASKET).text
        assert book_name == book_basket, "Имя в корзине и в каталоге не совпадают"

    def should_be_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_BASKET).text
        assert book_price == basket_price, "Цена в корзине и в каталоге не совпадают"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be--Сообщение об успехе есть. но не должно быть"

    def is_dissappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
