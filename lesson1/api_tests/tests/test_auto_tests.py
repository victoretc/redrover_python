import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from conftest import url

def test_get_by_endpoint():
    response = requests.get(url)
    assert response.status_code == 200
def test_get_by_selector():
    browser = webdriver.Chrome()
    browser.get(url)
    # time.sleep(5)
    assert url == "http://localhost:5173/", "URLs do not match"


# @pytest.fixture
# def setup():
#     browser = webdriver.Chrome()
#     browser.get(url)
#     yield browser
#     browser.quit()

def test_add_test_case(setup):
    driver = setup

    # Fill in the "Name" field
    name_field = driver.find_element(By.ID, "name")
    name_field.clear()
    name_field.send_keys("Test Case 1")

    # Fill in the "Description" field
    description_field = driver.find_element(By.ID, 'description')
    description_field.clear()
    description_field.send_keys("Test Case 99 Description")

    # Fill in the steps
    steps_field = driver.find_element(By.ID, 'steps')
    steps_field.clear()
    steps_field.send_keys("Open home page, check navigation bar, check header, check content body, check footer")

    # Fill in the "Expected Result" field
    expected_result_field = driver.find_element(By.ID, "expected_result")
    expected_result_field.clear()
    expected_result_field.send_keys("UI should be visible and clickable")

    # Select priority
    priority_dropdown = driver.find_element(By.ID, "priority")
    priority_dropdown.click()
    priority_options = driver.find_element(By.XPATH, "//option[text()='высокий']")
    priority_options.click()

    # Click the "Add Test Case" button
    add_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    add_button.click()

    # Validation Table Data 
    # TODO : example 1 >>
    # table_row_name = driver.find_element(By.XPATH, "//td[text()='Test Case 1']")
    # assert table_row_name is not None, "Row not found" and table_row_name.text == "Test Case 1"
    # TODO : example 2 >>
    table = driver.find_element(By.XPATH, "//td")
    assert table is not None, "Row not found" and "Test Case 1" in table.text
    assert table is not None, "Row not found" and "Test Case 1 Description" in table.text
    assert table is not None, "Row not found" and "UI should be visible and clickable" in table.text
    assert table is not None, "Row not found" and "средний" in table.text

    time.sleep(5)

def test_delete_test_case(setup):
    driver = setup
    id_str = '1'

    # rows = driver.find_elements(By.XPATH, "//table/tbody")
    # for i, row in enumerate(rows):
    #     print(f"Row {i}: {row.text}")
    # table_id = driver.find_element(By.XPATH, f"//td[text()={id_str}]")
    # assert table_id is not None, "The specified ID was not found in the table."

    # TODO : Click the "Delete" button 
    # delete_button = driver.find_element(By.XPATH, f"//table/tbody/tr/td[text()='{id_str}']//td/button[@class='btn btn-danger']")
    delete_button = driver.find_element(By.XPATH, "//button[text()='Удалить']")
    # delete_button = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    delete_button.click()
    time.sleep(2)


    assert id_str not in driver.find_element(By.XPATH, f"//td[text()='{id_str}']").text
