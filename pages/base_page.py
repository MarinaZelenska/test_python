import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setUp')
class BasePage(object):
    time_to_wait = 150
    sync_timeout = 30

    def __init__(self, setUp):
        self.driver = setUp

    def complete_field(self, locator, value):
        WebDriverWait(self.driver, self.time_to_wait).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        input_field = self.driver.find_element(*locator)
        input_field.click()
        input_field.send_keys(value)

    def select_button(self, locator):
        element = self.driver.find_element(locator)
        element.click()


