from lesson4.components import header, register
from lesson4.core.settings import settings
import allure
from faker import Faker

fake = Faker()


@allure.title("Регистрация")
def test_register():
    # main page 
    header.visit()
    header.should_be_opened()
    header.open_registration_component()
    # register form 
    register.type_login(fake.user_name())
    register.type_password(settings.register_password)
    register.type_confirm_password(settings.register_password)
    register.choose_tutor_role()
    register.click_register_button()
    # check result
    header.create_post_button_should_be_visible()

