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
