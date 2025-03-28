import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_register_positive(driver, wait):
    # main page
    driver.get('http://195.133.27.184/')
    assert driver.title == "Объявления"

    toggler_nav_locator = "//*[text()='Регистрация']"
    driver.find_element(By.XPATH, toggler_nav_locator).click()

    # registration form
    page_title_locator = "//h1[text() = 'Регистрация']"
    page_title = wait.until(EC.visibility_of_element_located((By.XPATH, page_title_locator)))
    assert page_title.text == "Регистрация"

    # input username
    login_locator = "//*[@placeholder = 'Введите имя пользователя']"
    driver.find_element(By.XPATH, login_locator).send_keys("Jerry")  # John exists

    # input password
    password_locator = "//*[@placeholder = 'Введите пароль']"
    driver.find_element(By.XPATH, password_locator).send_keys("Iamateacher")  # password is too spread

    # confirm password
    confirm_password_locator = "//*[@placeholder = 'Подтвердите пароль']"
    driver.find_element(By.XPATH, confirm_password_locator).send_keys("Iamateacher")

    # click check-box is_tutor
    check_box_locator = "//*[@name = 'is_tutor']"
    check_box = driver.find_element(By.XPATH, check_box_locator)
    if not check_box.is_selected():
        check_box.click()

    # submit form
    submit_btn_locator = "//*[@type = 'submit']"
    driver.find_element(By.XPATH, submit_btn_locator).click()

    # new page opens
    logout_btn_locator = "//*[text() = 'Выйти']"
    logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, logout_btn_locator)))
    assert logout_btn.is_displayed()


# NEGATIVE scenarios

# FOR TEACHER

def test_register_teacher_check_box(driver, wait):

    toggler_nav_locator = "//*[text()='Регистрация']"
    driver.find_element(By.XPATH, toggler_nav_locator).click()

    # registration form
    page_title_locator = "//h1[text() = 'Регистрация']"
    page_title = wait.until(EC.visibility_of_element_located((By.XPATH, page_title_locator)))
    assert page_title.text == "Регистрация"

    # input username
    login_locator = "//*[@placeholder = 'Введите имя пользователя']"
    driver.find_element(By.XPATH, login_locator).send_keys("Jerry")  # John exists

    # input password
    password_locator = "//*[@placeholder = 'Введите пароль']"
    driver.find_element(By.XPATH, password_locator).send_keys("Iamateacher")  # password is too spread

    # confirm password
    confirm_password_locator = "//*[@placeholder = 'Подтвердите пароль']"
    driver.find_element(By.XPATH, confirm_password_locator).send_keys("Iamateacher")

    # click check-box is_tutor
    check_box_locator = "//*[@name = 'is_tutor']"
    check_box = driver.find_element(By.XPATH, check_box_locator)
    if not check_box.is_selected():
        check_box.click()

    # submit form
    submit_btn_locator = "//*[@type = 'submit']"
    driver.find_element(By.XPATH, submit_btn_locator).click()

    # new page opens
    logout_btn_locator = "//*[text() = 'Выйти']"
    logout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, logout_btn_locator)))
    assert logout_btn.is_displayed()


### FOR STUDENT
@pytest.mark.parametrize("username, password, confirm_password, expected", [
    ("", "", "", "Обязательное поле."),
    ("Jerry", "", "", "Пользователь с таким именем уже существует."),
    ("", "qwertyuiop", "qwertyuiop", "Обязательное поле."),
    # ("123456", "qwertyuiop", "qwertyuiop", " ? ")  # ? should be an error. In fact, it passes
])
def test_register_student_username_negative(driver, wait, username, password, confirm_password, expected):
    # main page
    toggler_nav_locator = "//*[text()='Регистрация']"
    driver.find_element(By.XPATH, toggler_nav_locator).click()

    # registration form
    page_title_locator = "//h1[text() = 'Регистрация']"
    page_title = wait.until(EC.visibility_of_element_located((By.XPATH, page_title_locator)))
    assert page_title.text == "Регистрация"

    # input username
    login_locator = "//*[@placeholder = 'Введите имя пользователя']"
    driver.find_element(By.XPATH, login_locator).send_keys(username)

    # input password
    password_locator = "//*[@placeholder = 'Введите пароль']"
    driver.find_element(By.XPATH, password_locator).send_keys(password)

    # confirm password
    confirm_password_locator = "//*[@placeholder = 'Подтвердите пароль']"
    driver.find_element(By.XPATH, confirm_password_locator).send_keys(confirm_password)

    # submit form
    submit_btn_locator = "//*[@type = 'submit']"
    driver.find_element(By.XPATH, submit_btn_locator).click()

    error_message_locator = f"//*[text() = '{expected}']"
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, error_message_locator)))
    assert error_message.text == expected


@pytest.mark.parametrize("username, password, confirm_password, expected", [
    ("Nina", "qwertyuiop", "qwertyuiop", "Введённый пароль слишком широко распространён."),
    ("Nina", "12345678", "12345678", "Введённый пароль слишком широко распространён."),
    ("Nina", "poiuytre", "poiuytr", "Введенные пароли не совпадают."),
    ("Nina", "poiuytre", "poiuytree", "Введенные пароли не совпадают."),
    ("Nina", "qwertyu", "qwertyu", "Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.")
])
def test_register_student_password_negative(driver, wait, username, password, confirm_password, expected):
    # main page
    toggler_nav_locator = "//*[text()='Регистрация']"
    driver.find_element(By.XPATH, toggler_nav_locator).click()

    # registration form
    page_title_locator = "//h1[text() = 'Регистрация']"
    page_title = wait.until(EC.visibility_of_element_located((By.XPATH, page_title_locator)))
    assert page_title.text == "Регистрация"

    # input username
    login_locator = "//*[@placeholder = 'Введите имя пользователя']"
    driver.find_element(By.XPATH, login_locator).send_keys(username)

    # input password
    password_locator = "//*[@placeholder = 'Введите пароль']"
    driver.find_element(By.XPATH, password_locator).send_keys(password)

    # confirm password
    confirm_password_locator = "//*[@placeholder = 'Подтвердите пароль']"
    driver.find_element(By.XPATH, confirm_password_locator).send_keys(confirm_password)

    # submit form
    submit_btn_locator = "//*[@type = 'submit']"
    driver.find_element(By.XPATH, submit_btn_locator).click()

    error_message_locator = f"//*[text() = '{expected}']"
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, error_message_locator)))
    assert error_message.text == expected
