import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.action_chains import ActionChains


from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import sign_up_locators as loc
from selenium.webdriver.common.keys import Keys


class SignUpPage(BasePage):

    def fill_sign_up_fields(self, first_name, last_name, email, password):
        frame_1 = self.driver.find_element_by_xpath('//ui-registration-form')
        self.driver.switch_to.frame(frame_1)
        self.complete_field(loc.FIRST_NAME_FIELD, first_name)
        self.complete_field(loc.LAST_NAME_FIELD, last_name)
        self.complete_field(loc.EMAIL_FIELD, email)
        self.complete_field(loc.PASSWORD_FIELD, password)

    def check(self):
        action = ActionChains(self.driver)
        action.click(loc.FIRST_NAME_FIELD)

    def click_sign_up_button(self):
        self.select_button(loc.SIGN_UP_BUTTON)

    def complete_checkbox(self):
        self.select_button(loc.POLICY_CONFIRM_CHECKBOX)

    def check_element_visibility(self, element):
        item = self.CHECK[element]
        try:
            self.driver.find_element(*item)
            return True
        except NoSuchElementException:
            return False

    def click_seach(self):
        time.sleep(5)
        b = self.driver.find_element_by_xpath('//button[@data-id="searchBox"]')
        b.click()
