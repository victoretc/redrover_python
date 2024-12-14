from selene import by, be, have, browser
from lesson4.core.settings import settings
import allure

@allure.step("Открываем Хедер на главной странице")
def visit():
    browser.open('/')

@allure.step("Проверяем открытие Хедера")
def should_be_opened():
    browser.should(have.url(settings.base_url))

@allure.step("Открываем форму регистрации")
def open_registration_component():
    browser.element(by.text('Регистрация')).click()
    #browser.element(by.xpath("//a[@data-testid='signup']"))

@allure.step("Проверяем видимость кнопки создания объявления")
def create_post_button_should_be_visible():
    browser.element(by.text('Создать объявление')).should(be.visible)