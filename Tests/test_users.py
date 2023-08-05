import pytest
from Pages.LoginPage import LoginPage
from Reports.Log import Logger


class TestUsers:

    @pytest.fixture(scope="class", autouse=True)
    def set_up(self, driver):
        driver.get('https://www.saucedemo.com/inventory.html')
        yield
        driver.quit()

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

    @pytest.mark.parametrize("username, password",
                             [('standard_user', 'secret_sauce'),
                              ('locked_out_user', 'secret_sauce'),
                              ('problem_user', 'secret_sauce'),
                              ('performance_glitch_user', 'secret_sauce')])
    def test_all_users_items_display(self, driver, username, password):
        """
        Test checks if it's possible to log in with other usernames
        """

        login_page = LoginPage(driver)
        inventory_page = login_page.login(username, password)
        items_images_dict = inventory_page.get_items_images_dict()
        assert inventory_page.check_products_page_displayed()

        inventory_page.logout()




if __name__ == '__main__':
    pytest.main()
