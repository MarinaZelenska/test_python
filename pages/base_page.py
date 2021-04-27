import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setUp')
class BasePage(object):
    time_to_wait = 5

    def __init__(self, setUp):
        self.driver = setUp

    def complete_field(self, locator, value):
        WebDriverWait(self.driver, self.time_to_wait).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        input_field = self.driver.find_element(*locator)
        input_field.click()
        input_field.send_keys(value)

    def click_button(self, locator):
        WebDriverWait(self.driver, self.time_to_wait).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        element = self.driver.find_element(*locator)
        element.click()

    def check_element_visibility(self, element):
        item = self.CHECK[element]
        WebDriverWait(self.driver, self.time_to_wait).until(
            expected_conditions.visibility_of_element_located(item)
        )
        try:
            self.driver.find_element(*item)
            return True
        except NoSuchElementException:
            return False
