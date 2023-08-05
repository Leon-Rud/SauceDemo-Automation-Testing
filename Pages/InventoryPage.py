from Pages.BasePage import BasePage
from Reports.Log import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Pages.CartPage import CartPage
from Objects.Products import Product

# Locators for Inventory Page
inv_list = (By.CLASS_NAME, 'inventory_item_description')
item_price = (By.CLASS_NAME, 'inventory_item_price')
sort_menu = (By.XPATH, '//*[@data-test="product_sort_container"]')
shop_cart = (By.ID, 'shopping_cart_container')
logout_button = (By.ID, 'logout_sidebar_link')
burger_button = (By.CLASS_NAME, 'bm-burger-button')
items_names = (By.CLASS_NAME, 'inventory_item_name')
high_to_low = 'hilo'
low_to_high = 'lohi'
a_to_z = 'a-z'
z_to_a = 'z-a'




class InventoryPage(BasePage):

    clothing_items_list = ['Jacket', 'Shirt', 'Onesie']

    # TODO Add private methods

    def __init__(self, driver):
        super().__init__(driver)

    def logout(self):
        self.click_element(burger_button)
        self.click_element(logout_button)

    def check_products_page_displayed(self):
        return self.check_text_presence_in_page('Products')

    def get_current_added_items(self):
        added_items_list = []
        items = self.get_inventory_elements()
        for item in items:
            item_name = item.text.split('\n')[0]
            if self.check_item_added_by_name(item_name):
                added_items_list.append(self.get_item_price_dict(item_name))

        return added_items_list

    def click_on_cart_button(self):
        self.click_element(shop_cart)
        return CartPage(self.driver)

    def get_item_price_dict(self, item_name):
        parent_element = self.get_parent_element_by_item_name(item_name)
        prices_dict = {}
        prices_el = parent_element.find_element(*item_price)
        price = float(prices_el.text.strip('$'))
        prices_dict[item_name] = price

        return prices_dict

    def add_second_most_expensive_item(self):
        items = self.get_inventory_elements()
        return self.add_item_to_cart_by_index(items, 1)

    def add_third_most_expensive_item(self):
        items = self.get_inventory_elements()
        return self.add_item_to_cart_by_index(items, 2)

    # sort list -> add all clothes to list -> add most expensive clothing item to cart
    def add_most_expensive_clothing_item(self):
        # Get clothing list after sorting
        clothes_list = self.get_list_by_item_names(self.clothing_items_list)
        # add most expensive item to cart
        return self.add_item_to_cart_by_index(clothes_list, 0)

    def add_item_to_cart_by_index(self, items_list: list, index: int):
        # get element of most expensive price clothing item
        most_expensive_item = items_list[index]
        # add most expensive item to cart
        return self.add_to_cart(most_expensive_item)

    def get_list_by_item_names(self, item_names: list):
        clothing_items = []
        items = self.get_inventory_elements()
        for item in items:
            # add all items that contain the items of the received list
            if [item_name for item_name in item_names if item_name in item.text]:
                clothing_items.append(item)

        return clothing_items

    def sort_by_highest(self):
        self.sort_by_value(high_to_low)

    def sort_by_value(self, sort_option: str):
        select_sort_menu = Select(self.get_element(sort_menu))
        select_sort_menu.select_by_value(sort_option)

    def get_items_price_list(self):
        items_price = []
        price_elements = self.get_elements(item_price)
        for price in price_elements:
            items_price.append(float(price.text.strip('$')))

        return items_price

    def check_list_sorted(self, sorted_list: list):
        items_price_list = self.get_items_price_list()
        return items_price_list == sorted(sorted_list, reverse=True)

    def add_to_cart(self, parent_element):
        add_to_cart_btn = parent_element.find_element(By.TAG_NAME, 'button')
        add_to_cart_btn.click()
        # get element after click to avoid "element is not attached to the page document"
        add_to_cart_btn = parent_element.find_element(By.TAG_NAME, 'button')
        # create Product instance if item added
        if add_to_cart_btn.text == 'Remove':
            return self.get_product_info(parent_element)
        Logger.log.error('Button text didn\'t change to remove')
        return False

    def get_product_info(self, parent_element):
        product_fields = parent_element.text.split('\n')
        Product.name = product_fields[0]
        Product.price = float(product_fields[2].strip('$'))
        return Product.name, Product.price

    def check_item_added_by_name(self, item_name):
        parent_item = self.get_parent_element_by_item_name(item_name)
        button = parent_item.find_element(By.TAG_NAME, 'button')
        # create Product instance if item added
        if button.text == 'Remove':
            return True
        return False

    def get_parent_element_by_item_name(self, item_name: str):
        child_item = self.get_element((By.XPATH, f'//*[contains(text(), "{item_name}")]'))
        parent_item = child_item.find_element(By.XPATH, '../../..')
        return parent_item

    def remove_item_by_name(self, item_name):
        parent_item = self.get_parent_element_by_item_name(item_name)
        parent_item.find_element(By.TAG_NAME, 'button').click()

    def get_inventory_elements(self):
        return self.get_elements(inv_list)

    def get_items_images_dict(self):
        items_images_dict = {}
        items_names_ele = self.get_elements(items_names)
        items_images_ele = self.get_elements((By.TAG_NAME, 'img'))
        for index, item in items_names_ele:
            items_images_dict[item] = items_images_ele[index]

