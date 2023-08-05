from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

# Locators for Checkout Page
first_name_field = (By.ID, 'first-name')
last_name_field = (By.ID, 'last-name')
postal_code_field = (By.ID, 'postal-code')
continue_btn = (By.ID, 'continue')
checkout_total = (By.CLASS_NAME, 'summary_subtotal_label')
finish_btn = (By.ID, 'finish')
back_home_btn = (By.ID, 'back-to-products')


class CheckoutPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_back_home(self):
        self.click_element(back_home_btn)
        # To avoid circuler imports
        from Pages.InventoryPage import InventoryPage
        return InventoryPage(self.driver)

    def check_thank_you_message(self):
        return self.check_text_presence_in_page('Your order has been dispatched, and will arrive just as fast as the'
                                                ' pony can get there!')

    def click_finish_button(self):
        self.click_element(finish_btn)

    def get_items_total(self):
        item_text = self.get_element(checkout_total).text
        return float(item_text.split('$')[1])

    def click_continue_button(self):
        self.click_element(continue_btn)

    def fill_information(self, first_name: str, last_name: str, postal_code: int):

        '''
        Fill first name, last name and postal code in check out page
        '''

        self.send_keys(first_name_field, first_name)
        self.send_keys(last_name_field, last_name)
        self.send_keys(postal_code_field, postal_code)

        return first_name, last_name, postal_code
