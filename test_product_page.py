from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLocators.PRODUCT_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_correct_success_message()
    page.should_be_correct_price_for_product()
