import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time


@pytest.fixture(scope="session")
def load_person_date():
    # Открываем файл с конфигом в режиме чтения
    with open('person.json', 'r') as config_file:
        # С помощью библиотеки json читаем и возвращаем результат
        config = json.load(config_file)
        return config

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()