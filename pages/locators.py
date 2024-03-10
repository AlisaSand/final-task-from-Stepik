from selenium.webdriver.common.by import By

class MainPageLocators():
    LINK = 'https://selenium1py.pythonanywhere.com/'
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LINK = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators:
    PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    CART_BOOK_NAME = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    CART_COST = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    BOOK_TITLE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    BOOK_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
