import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "http://localhost:5173/"

@pytest.fixture
def setup():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()