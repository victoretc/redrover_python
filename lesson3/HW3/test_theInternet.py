import time
from logging import exception

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import conftest
import requests


def test_add_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    button_add = driver.find_element(By.XPATH, "//button")
    button_add.click()

    button_del = driver.find_element(By.XPATH, "//button[@class='added-manually']")

    assert button_del.is_displayed()

def test_del_element(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    button_add = driver.find_element(By.XPATH, "//button")
    button_add.click()

    button_del = driver.find_element(By.XPATH, "//button[@class='added-manually']")
    button_del.click()

    try:
        button_del_check  = driver.find_element(By.XPATH, "//button[@class='added-manually']").is_displayed()
    except NoSuchElementException:
        button_del_check = False

    assert button_del_check == False

def test_authorisation(driver):
    login = "admin"
    passw = "admin"
    driver.get(f'https://{login}:{passw}@the-internet.herokuapp.com/basic_auth')

    message = driver.find_element(By.XPATH, "//p").text

    assert message == "Congratulations! You must have the proper credentials."

def test_check_box(driver):
    check_box1_locator = "//input[@type='checkbox'][1]"
    check_box2_locator = "//input[@type='checkbox'][2]"

    driver.get("https://the-internet.herokuapp.com/checkboxes")
    option1 = driver.find_element(By.XPATH, check_box1_locator)
    option2 = driver.find_element(By.XPATH, check_box2_locator)

    option1.click()
    if not option2.is_selected():
        option2.click()

    assert option1.is_selected() == True
    assert option2.is_selected() == True


def test_pics(driver):
    driver.get("https://the-internet.herokuapp.com/broken_images")
    all_links = driver.find_elements(By.XPATH, "//img[contains(@src,'.jpg')]")

    for link in all_links:
        url = link.get_attribute('src')
        result = requests.head(url)

        try:
            result = requests.head(url)
            assert result.status_code == 200
        except AssertionError:
            print(url, result.status_code)










