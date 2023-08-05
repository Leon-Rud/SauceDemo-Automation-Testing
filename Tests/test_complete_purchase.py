import pytest
from Pages.LoginPage import LoginPage
from Reports.Log import Logger


# TODO update project description more in depth about best prectices: reports, POM, logs, fixtures,etc.


class TestCompletePurchase:

    @pytest.fixture(scope="class", autouse=True)
    def set_up(self, driver):
        driver.get('https://www.saucedemo.com/inventory.html')
        yield
        driver.quit()

    @pytest.mark.parametrize("username, password",
                             [('standard_user', 'secret_sauce')])
    def test_purchase_flow(self, driver, username, password):

        """
        1. Mike got $50 as a Christmas gift and decided to add the most expensive piece of clothing to his cart
        (using the site's sorting).
        2. Mike reconsidered, removed the item and decided to add the second most expensive item to the cart and the
        next item in the list as well
        3. Mike clicks on cart button and verifies that the correct product (name and cost) are added in the cart
        + verify adding/removing items are done correctly ->
        4. Mike navigate to the checkout page, adds personal information and verifies correct item total displayed
        5. Mike clicks on finish and verifies order is complete and thank you message is displayed
        """

        Logger.log.info('STEP 1 - Add most expensive item to cart')
        login_page = LoginPage(driver)
        inventory_page = login_page.login(username, password)
        # sort list by highest price
        inventory_page.sort_by_highest()
        item_prices_list = inventory_page.get_items_price_list()
        # check if list is sorted by highest price
        assert inventory_page.check_list_sorted(item_prices_list)
        # check item is added and REMOVE button is displayed
        most_exp_item_name, most_exp_item_price = inventory_page.add_most_expensive_clothing_item()
        # check most expensive item added
        assert(most_exp_item_name, most_exp_item_price) == ('Sauce Labs Fleece Jacket', 49.99)
        assert inventory_page.check_item_added_by_name('Sauce Labs Fleece Jacket')

        Logger.log.info('STEP 2 - Remove item, add the second most expensive item and the next item')
        inventory_page.remove_item_by_name('Sauce Labs Fleece Jacket')
        # Check Remove button isn't displayed
        assert not inventory_page.check_item_added_by_name('Sauce Labs Fleece Jacket')
        # Add items
        second_exp_item_name, second_exp_item_price = inventory_page.add_second_most_expensive_item()
        third_exp_item_name, third_exp_item_price = inventory_page.add_third_most_expensive_item()
        assert second_exp_item_name, third_exp_item_name == ('Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt')
        assert second_exp_item_price > third_exp_item_price
        assert inventory_page.check_item_added_by_name('Sauce Labs Backpack')
        assert inventory_page.check_item_added_by_name('Sauce Labs Bolt T-Shirt')

        Logger.log.info('STEP 3 - Verify the correct product (name and cost) are added in the cart')
        added_items_dict = inventory_page.get_current_added_items()
        cart_page = inventory_page.click_on_cart_button()
        cart_page.check_items_in_cart(added_items_dict)

        Logger.log.info('STEP 4 - Add personal information and verify correct item total displayed')
        cart_items_total = cart_page.get_items_total(added_items_dict)
        checkout_page = cart_page.click_on_checkout_button()
        Mike_info = 'Mike', 'Johnson', 12345
        first_name, last_name, postal_code = checkout_page.fill_information(*Mike_info)
        assert (first_name, last_name, postal_code) == (Mike_info)
        checkout_page.click_continue_button()
        checkout_items_total = checkout_page.get_items_total()
        assert cart_items_total == checkout_items_total

        Logger.log.info('STEP 5 - Click on finish and verify order is complete with thank you message')
        checkout_page.click_finish_button()
        assert checkout_page.check_thank_you_message()
        Logger.log.info('Test finished successfully')
        inventory_page = checkout_page.click_back_home()
        inventory_page.logout()

    @pytest.mark.parametrize("username, password",
                             [('standard_user', 'secret_sauce'),
                              ('locked_out_user', 'secret_sauce'),
                              ('problem_user', 'secret_sauce'),
                              ('performance_glitch_user', 'secret_sauce')])
    def test_all_users_login(self, driver, username, password):

        """
        Test checks if it's possible to log in with other usernames
        """

        login_page = LoginPage(driver)
        inventory_page = login_page.login(username, password)
        error_message = f'User: "{username}" couldn\'t login the site'
        success_message = f'User: "{username}" successfully logged in the site'
        assert inventory_page.check_products_page_displayed(), error_message
        Logger.log.info(success_message)

        inventory_page.logout()