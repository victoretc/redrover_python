from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_visible_after_with_explicit_waits_with_selenium(driver, wait):
    driver.get('https://demoqa.com/dynamic-properties')
    visible_after_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Visible After 5 Seconds']")))
    assert visible_after_button.text == 'Visible After 5 Seconds'
