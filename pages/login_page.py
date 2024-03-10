from .base_page import BasePage
from .main_page import MainPage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url(self.browser)
        self.should_be_login_form(self.browser)
        self.should_be_register_form(self.browser)

    def should_be_login_url(self, browser):
        link = LoginPageLocators.LINK
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_url()
        # реализуйте проверку на корректный url адрес
        # assert True

    def should_be_login_form(self, browser):
        link = MainPageLocators.LINK
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_form()
        # реализуйте проверку, что есть форма логина
        # assert True

    def should_be_register_form(self, browser):
        link = MainPageLocators.LINK
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_registration_form()
        # реализуйте проверку, что есть форма регистрации на странице
        # assert True