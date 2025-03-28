from selene import be, have, browser
import allure


@allure.step("Открываем форму регистрации")
def visit():
    browser.open('/signup/')


@allure.step("Проверяем открытие формы регистрации")
def should_be_opened():
    browser.should(have.url('/signup/'))


@allure.step("Вводим логин")
def type_login(login):
    browser.element('#id_username').type(login)


@allure.step("Вводим пароль")
def type_password(password):
    browser.element('#id_password1').type(password)


@allure.step("Вводим подтверждение пароля")
def type_confirm_password(password):
    browser.element('#id_password2').type(password)


@allure.step("Выбираем роль учителя")
def choose_tutor_role():
    checkbox = browser.element('#id_is_tutor')
    checkbox.click()
    checkbox.should(be.selected)


@allure.step("Нажимаем кнопку регистрации")
def click_register_button():
    browser.element('button[type="submit"]').click()
