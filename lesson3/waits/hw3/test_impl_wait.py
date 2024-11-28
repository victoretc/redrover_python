import time

from selenium.webdriver.common.by import By
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
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_registration(driver):
    # Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/
    # Проверить заголовок: Убедиться, что текст в теге
    driver.get("https://victoretc.github.io/selenium_waits/")
    title = driver.find_element(By.XPATH, "//h1[text()= 'Практика с ожиданиями в Selenium']")
    assert title.text == 'Практика с ожиданиями в Selenium'

    # Дождаться появления кнопки "Начать тестирование"
    # Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    # Кликнуть по кнопке "Начать тестирование".
    start_test_btn = driver.find_element(By.XPATH, "//button[@id='startTest']")
    start_test_btn.click()

    login = driver.find_element(By.XPATH, "//*[@for='login']")
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

    time.sleep(5)

    # Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    success_registration = driver.find_element(By.XPATH, "//*[@id='successMessage']")
    assert success_registration.is_displayed()
    assert success_registration.text == 'Вы успешно зарегистрированы!'


def test_registration1(driver):
    try:
        # 1. Переходим на сайт
        driver.get('https://victoretc.github.io/selenium_waits/')

        # 2. Проверяем заголовок страницы
        assert "Практика Selenium" in driver.title, "Заголовок страницы не совпадает"

        # 3. Ждем появления кнопки "Начать тестирование"
        # Убедимся, что кнопка присутствует на странице
        start_testing_button = driver.find_element(By.XPATH, "//button[text()='Начать тестирование']")

        # 4. Кликаем по кнопке "Начать тестирование"
        start_testing_button.click()

        # 5. Вводим логин в поле для логина
        login_field = driver.find_element(By.XPATH, "//*[@id='login']")
        login_field.send_keys('login')

        # 6. Вводим пароль в поле для пароля
        password_field = driver.find_element(By.XPATH, "//*[@id='password']")
        password_field.send_keys('password')

        # 7. Устанавливаем флажок "Согласен со всеми правилами"
        agree_checkbox = driver.find_element(By.XPATH, "//*[@id='agree']")
        if not agree_checkbox.is_selected():
            agree_checkbox.click()

        # 8. Нажимаем кнопку "Зарегистрироваться"
        register_button = driver.find_element(By.XPATH, "//*[@id='register']")
        register_button.click()

        # 9. Проверяем наличие индикатора загрузки
        loading_indicator = driver.find_element(By.XPATH, "//*[@id='loader']")  # Пример ID для индикатора
        assert loading_indicator.is_displayed(), "Индикатор загрузки не отображается"

        # 10. Ждем завершения загрузки и появления сообщения о успешной регистрации
        time.sleep(5)  # Ожидаем, что индикатор загрузки исчезнет

        # 11. Проверяем сообщение о успешной регистрации
        success_message = driver.find_element(By.XPATH, "//*[@id='successMessage']")
        assert success_message.is_displayed(), "Сообщение об успешной регистрации не появилось"

        print("Тест прошел успешно!")

    finally:
        # Закрываем браузер
        driver.quit()
