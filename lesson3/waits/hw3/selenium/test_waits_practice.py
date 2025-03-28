import time
import requests

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument("--window-size=1900x1000")
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


def test1(driver, wait):
    driver.get("https://www.selenium.dev/selenium/web/dynamic.html")
    add_box_locator = "//*[@value = 'Add a box!']"
    box_locator = "//div[contains(@id, 'box')]"

    add_box = wait.until(EC.visibility_of_element_located((By.XPATH, add_box_locator)))
    assert add_box.is_displayed()
    assert add_box.get_attribute("value") == 'Add a box!'

    lst = []
    add_box.click()
    box = wait.until(EC.visibility_of_element_located((By.XPATH, box_locator)))
    lst.append(box)
    count = 1

    add_box.click()
    lst.append(box)
    count += 1
    assert len(lst) == count


def test2(driver, wait):
    driver.get("https://demoqa.com/dynamic-properties")
    will_enable_5sec_locator = "//*[@id = 'enableAfter']"

    will_enable_5sec_btn = wait.until(EC.visibility_of_element_located((By.XPATH, will_enable_5sec_locator)))
    assert will_enable_5sec_btn.is_displayed()


def test3(driver, wait):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading")
    assert driver.title == "The Internet"

    hidden_element_locator = "//*[contains(text(), 'Element on page that is hidden')]"
    start_btn_locator = "//*[contains(text(), 'Start')]"
    loading_indicator_locator = "//*[@id = 'loading']"
    hello_world_locator = "//*[contains(text(), 'Hello World!')]"

    hidden_element = wait.until(EC.element_to_be_clickable((By.XPATH, hidden_element_locator)))
    hidden_element.click()

    start_btn = wait.until(EC.element_to_be_clickable((By.XPATH, start_btn_locator)))
    assert start_btn.is_enabled()
    start_btn.click()

    loading_indicator = wait.until(EC.visibility_of_element_located((By.XPATH, loading_indicator_locator)))
    assert loading_indicator.is_displayed()

    hello_world = wait.until(EC.visibility_of_element_located((By.XPATH, hello_world_locator)))
    assert hello_world.is_displayed()


# 1. <https://the-internet.herokuapp.com/add_remove_elements/> (Необходимо создать и удалить элемент)
def test4(driver, wait):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element_btn_locator = "//*[@onclick= 'addElement()']"
    delete_btn_locator = "//*[@onclick= 'deleteElement()']"
    add_element = wait.until(EC.element_to_be_clickable((By.XPATH, add_element_btn_locator)))
    add_element.click()
    delete_btn = wait.until(EC.element_to_be_clickable((By.XPATH, delete_btn_locator)))
    delete_btn.click()
    assert wait.until(EC.invisibility_of_element_located((By.XPATH, delete_btn_locator)))


# 2. <https://the-internet.herokuapp.com/basic_auth> (Необходимо пройти базовую авторизацию)
# (NOT CLEAR)
def test5(driver, wait):
    username = "admin"
    password = "admin"

    url = f"http://{username}:{password}@the-internet.herokuapp.com/basic_auth"
    title_locator = "//*[text()='Basic Auth']"

    driver.get(url)
    time.sleep(2)
    title = wait.until(EC.visibility_of_element_located((By.XPATH, title_locator)))
    assert title.text == "Basic Auth"


# 3. <https://the-internet.herokuapp.com/broken_images> (Необходимо найти сломанные изображения)
# (NOT CLEAR)
def test6(driver, wait):
    driver.get("https://the-internet.herokuapp.com/broken_images")

    image_locator = "//div/img"
    images = wait.until(EC.visibility_of_all_elements_located((By.XPATH, image_locator)))

    broken_images = []

    for i in images:
        src = i.get_attribute("src")

        response = requests.get(src)
        if response.status_code != 200 or response.status_code == 404:
            broken_images.append(src)

    assert len(broken_images) == 2


# 4. <https://the-internet.herokuapp.com/checkboxes> (Практика с чек боксами)
def test7(driver, wait):
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    check_boxs_locator = "//*[@type = 'checkbox']"
    check_boxs = wait.until(EC.visibility_of_all_elements_located((By.XPATH, check_boxs_locator)))

    for check_box in check_boxs:
        if not check_box.is_selected():
            check_box.click()
        assert check_box.is_selected()

    for check_box in check_boxs:
        check_box.click()
        assert not check_box.is_selected()
        time.sleep(2)
