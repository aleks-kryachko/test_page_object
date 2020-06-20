import math
from pages.base_page import BasePage
from locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_book_name()
        self.should_be_book_price()

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.add_button), "Кнопки добавить нет"
        button = self.browser.find_element(*ProductPageLocators.add_button)
        button.click()

    def solve_quiz_and_get_code(self):
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
        book_name = self.browser.find_element(*ProductPageLocators.book_name).text
        book_basket = self.browser.find_element(*ProductPageLocators.book_name_basket).text
        assert book_name == book_basket, "Имя в корзине и в каталоге не совпадают"

    def should_be_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.book_price).text
        basket_price = self.browser.find_element(*ProductPageLocators.book_price_basket).text
        assert book_price == basket_price, "Цена в корзине и в каталоге не совпадают"
