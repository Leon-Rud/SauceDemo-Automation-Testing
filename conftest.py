from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
import tempfile
import pytest
import base64


@pytest.fixture(scope='class')
def driver():
    service = ChromeService(executable_path='/Users/leon/Desktop/chromedriver')
    driver = ChromeDriver(service=service)
    driver.maximize_window()
    yield driver

# pytest --html=report.html


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == 'call' and report.failed:
        driver = item.funcargs['driver']
        screenshot_path = create_screenshot(driver)
        with open(screenshot_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())
            padding = b'=' * (-len(encoded_string) % 4)
            encoded_string += padding
        extra.append(pytest_html.extras.image(encoded_string.decode('ascii')))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra


def create_screenshot(driver):
    with tempfile.NamedTemporaryFile(suffix='.png', delete=True) as f:
        screenshot_path = f.name
    driver.save_screenshot(screenshot_path)
    return screenshot_path
