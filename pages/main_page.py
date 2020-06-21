from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def go_to_login_page(self):  # чтобы иметь доступ к атрибутам и методам класса:
        # символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
        login_link = self.browser.find_element(*MainPageLocators.login_link)
        login_link.click()
        self.should_be_login_link()

    def should_be_login_link(self):   # перехватывать исключения.
        assert self.is_element_present(*MainPageLocators.login_link), "Login link is not presented"
#
