from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        product_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        product_link.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_success_message(self):
        cart_book_title = self.browser.find_element(*ProductPageLocators.CART_BOOK_NAME).text
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert cart_book_title == book_title, 'there is another book in a cart'

    def should_be_correct_price_for_product(self):
        cart_book_price = self.browser.find_element(*ProductPageLocators.CART_COST).text
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert cart_book_price == book_price, 'there is a cost of another book in a cart'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not to be"
