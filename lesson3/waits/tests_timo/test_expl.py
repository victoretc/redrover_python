from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


# ! : EXPLICIT waits

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=5)
    return wait

class TestExample:
    selector_start_test = "//button[@id='startTest']"
    selector_login = "//input[@id='login']"
    selector_password = "//input[@id='password']"
    selector_check_box_agree = "//input[@id='agree']"
    selector_reg_button = "//button[@id='register']"
    selector_loader = "//div[@id='loader']"
    selector_success = "//p[@id='successMessage']"

data = TestExample


def test_hw_expl(driver, wait):

    # Check title
    driver.get('https://victoretc.github.io/selenium_waits/')
    assert driver.title == "Практика Selenium"
    # Check start test button
    start_test_button = wait.until(EC.element_to_be_clickable((By.XPATH, data.selector_start_test)))
    assert start_test_button.text == "Начать тестирование"
    start_test_button.click()
    # Fill form
    driver.find_element(By.XPATH, data.selector_login).send_keys("login")
    driver.find_element(By.XPATH, data.selector_password).send_keys("password")
    # Check agree checkbox
    check_box = driver.find_element(By.XPATH, data.selector_check_box_agree)
    if not check_box.is_selected():
        check_box.click()
    driver.find_element(By.XPATH, data.selector_reg_button).click()
    # Check loader
    load_check = driver.find_element(By.XPATH, data.selector_loader)
    assert load_check.is_displayed()
    # Check success message
    success_check = wait.until(EC.element_to_be_clickable((By.XPATH, data.selector_success)))
    assert success_check.text == "Вы успешно зарегистрированы!"

    time.sleep(5)

    



