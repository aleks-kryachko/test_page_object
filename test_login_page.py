"""
pytest -v --tb=line --language=en test_login_page.py

"""
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

