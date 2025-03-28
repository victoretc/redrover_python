import time
from selenium.webdriver.common.by import By


def test_registration(driver):
    # Перейти по URL: Открыть в браузере указанный URL сайта https://victoretc.github.io/selenium_waits/
    # Проверить заголовок: Убедиться, что текст в теге
    driver.get("https://victoretc.github.io/selenium_waits/")
    title = driver.find_element(By.XPATH, "//h1[text()= 'Практика с ожиданиями в Selenium']")
    assert title.text == 'Практика с ожиданиями в Selenium'
    time.sleep(5)

    # Дождаться появления кнопки "Начать тестирование"
    # Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    begin_test_btn = driver.find_element(By.XPATH, "//button[@id='startTest']")
    assert begin_test_btn.is_displayed()
    assert begin_test_btn.text == 'Начать тестирование'

    # Кликнуть по кнопке "Начать тестирование".
    begin_test_btn.click()
    time.sleep(5)
    login = driver.find_element(By.XPATH, "//*[@for='login']")
    assert login.is_displayed()

    # Ввести "login" в поле для логина.
    login_field = driver.find_element(By.XPATH, "//*[@id='login']")
    login_field.send_keys("email")
    time.sleep(3)

    # Ввести "password" в поле для пароля.
    password_field = driver.find_element(By.XPATH, "//*[@id='password']")
    password_field.send_keys("password")
    time.sleep(3)

    # Установить флажок в чекбокс "Согласен со всеми правилами".
    check_box_agree = driver.find_element(By.XPATH, "//*[@id='agree']")
    check_box_agree.click()
    time.sleep(3)

    # Нажать кнопку "Зарегистрироваться".
    registration_btn = driver.find_element(By.XPATH, "//*[@id='register']")
    registration_btn.click()
    time.sleep(2)

    # Удостовериться, что появился индикатор загрузки.
    loader_indicator = driver.find_element(By.XPATH, "//*[@id='loader']")
    assert loader_indicator.is_displayed()
    time.sleep(5)

    # Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    success_registration = driver.find_element(By.XPATH, "//*[@id='successMessage']")
    assert success_registration.is_displayed()
    assert success_registration.text == 'Вы успешно зарегистрированы!'
