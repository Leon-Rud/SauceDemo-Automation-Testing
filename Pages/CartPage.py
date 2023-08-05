from Pages.BasePage import BasePage
from Pages.CheckoutPage import CheckoutPage
from selenium.webdriver.common.by import By

# Locators for Cart Page
cart_list = (By.CLASS_NAME, 'cart_item')
cart_price = (By.CLASS_NAME, 'inventory_item_price')
cart_buttons = (By.CLASS_NAME, 'cart_button')
checkout_button = (By.ID, 'checkout')


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_items_total(self, list_of_dicts: list):
        total = 0
        for dict in list_of_dicts:
            for value in dict.values():
                total += value

        return total

    def click_on_checkout_button(self):
        self.click_element(checkout_button)
        return CheckoutPage(self.driver)

    def check_items_in_cart(self, items_dict):
        items_in_cart = True
        for item in items_dict:
            for key, value in item.items():
                if not self.check_text_presence_in_page(key) and not self.check_text_presence_in_page(str(value)):
                    items_in_cart = False

        return items_in_cart
