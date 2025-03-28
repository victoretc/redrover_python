from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


def test_registration(driver, wait):
    # Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/
    # Проверить заголовок: Убедиться, что текст в теге
    driver.get("https://victoretc.github.io/selenium_waits/")
    title = driver.find_element(By.XPATH, "//h1[text()= 'Практика с ожиданиями в Selenium']")
    assert title.text == 'Практика с ожиданиями в Selenium'

    # Дождаться появления кнопки "Начать тестирование"
    # Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    begin_test_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='startTest']")))
    assert begin_test_btn.is_displayed()
    assert begin_test_btn.text == 'Начать тестирование'

    # Кликнуть по кнопке "Начать тестирование".
    begin_test_btn.click()
    login = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@for='login']")))

    assert login.is_displayed()

    # Ввести "login" в поле для логина.
    login_field = driver.find_element(By.XPATH, "//*[@id='login']")
    login_field.send_keys("email")

    # Ввести "password" в поле для пароля.
    password_field = driver.find_element(By.XPATH, "//*[@id='password']")
    password_field.send_keys("password")

    # Установить флажок в чекбокс "Согласен со всеми правилами".
    check_box_agree = driver.find_element(By.XPATH, "//*[@id='agree']")
    check_box_agree.click()

    # Нажать кнопку "Зарегистрироваться".
    registration_btn = driver.find_element(By.XPATH, "//*[@id='register']")
    registration_btn.click()

    # Удостовериться, что появился индикатор загрузки.
    loader_indicator = driver.find_element(By.XPATH, "//*[@id='loader']")
    assert loader_indicator.is_displayed()

    # Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    success_registration = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='successMessage']")))
    assert success_registration.is_displayed()
    assert success_registration.text == 'Вы успешно зарегистрированы!'
