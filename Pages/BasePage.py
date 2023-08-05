from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator: tuple, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.presence_of_element_located(locator))
        return element

    def get_elements(self, locator: tuple, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        elements = wait.until(EC.presence_of_all_elements_located(locator))
        return elements

    def click_element(self, locator: tuple, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        self.scroll_to_element(element)
        element.click()

    def send_keys(self, locator: tuple, text: str, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.element_to_be_clickable(locator))
        element.send_keys(element, text)

    def wait_and_switch_to_frame(self, locator, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def check_element_exists(self, locator, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def wait_for_page_load(self, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def check_text_presence_in_page(self, text: str):
        self.wait_for_page_load()
        page_source = self.driver.page_source
        if text in page_source:
            return True
        return False
