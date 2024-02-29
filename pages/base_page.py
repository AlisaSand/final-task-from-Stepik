from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, what, how):
        try:
            self.browser.find_element(what, how)
        except (NoSuchElementException):
            return False
        return True

    def is_url_correct(self):
        self.browser.find_element(By.ID,"login_link" ).click()


