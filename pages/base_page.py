import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setUp')
class BasePage(object):
    time_to_wait = 5

    def __init__(self, setUp):
        self.driver = setUp

    def complete_field(self, selector, value):
        WebDriverWait(self.driver, self.time_to_wait).until(
            expected_conditions.element_to_be_clickable(selector)
        )
        input_field = self.driver.find_element(*selector)
        input_field.click()
        input_field.send_keys(value)

    def click_button(self, selector):
        WebDriverWait(self.driver, self.time_to_wait).until(
            expected_conditions.visibility_of_element_located(selector)
        )
        element = self.driver.find_element(*selector)
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
