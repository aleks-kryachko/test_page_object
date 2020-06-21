from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_buttons()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*LoginPageLocators.login_link), "Login url is not presented"
        login_link = self.browser.find_element(*LoginPageLocators.login_link)
        login_link.click()
        assert "login" in self.browser.current_url, "Неправильный URL, нет Логина"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_form), "нет формы Логина"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации
        assert self.is_element_present(*LoginPageLocators.login_form), "нет формы Регистрации"

    def should_be_buttons(self):
        # проверка, что есть кнопки Вход и Зарегистрироваться
        assert self.is_element_present(*LoginPageLocators.button_enter), "Нет Кнопки Войти"
        assert self.is_element_present(*LoginPageLocators.button_registration), "Нет Кнопки Зарегистрироваться"