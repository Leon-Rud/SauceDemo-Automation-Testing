from Pages.BasePage import BasePage
from Pages.InventoryPage import InventoryPage
from selenium.webdriver.common.by import By

# Locators for Login Page
user_field = (By.NAME, 'user-name')
pass_field = (By.NAME, 'password')
login_button = (By.NAME, 'login-button')


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.user_field = self.get_element(user_field)
        self.pass_field = self.get_element(pass_field)
        self.login_button = self.get_element(login_button)

    def login(self, user_name, pass_name):
        self.user_field.clear()
        self.user_field.send_keys(user_name)
        self.pass_field.clear()
        self.pass_field.send_keys(pass_name)
        self.login_button.click()
        self.wait_for_page_load()
        return InventoryPage(self.driver)
