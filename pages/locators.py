from selenium.webdriver.common.by import By


class MainPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_link")
    login_form = (By.CSS_SELECTOR, "#login_form")
    button_enter =(By.NAME, "login_submit")
    button_registration = (By.NAME, "registration_submit")

class ProductPageLocators():
    add_button = (By.CSS_SELECTOR, ".btn-add-to-basket")
    book_name = (By.CSS_SELECTOR, ".product_main h1")
    book_price = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    book_name_basket = (By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")
    book_price_basket = (By.CSS_SELECTOR, "#messages>div:nth-child(3) strong")
    success_message = (By.CSS_SELECTOR, "#messages>div:nth-child(1)")