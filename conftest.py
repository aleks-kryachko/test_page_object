"""
RUN   pytest -v --tb=line --language=en test_main_page.py

"""
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None)

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
# ожидание чтобы визуально оценить на каком языке открылся браузер
    time.sleep(3)
    print("\nquit browser..")
    browser.quit()
