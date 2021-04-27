
from pages.base_page import BasePage
from pages.locators import sign_up_locators as loc, base_page_locators as locs


class SignUpPage(BasePage):
    CHECK = {
        'submit_code_button': loc.SUBMIT_CODE_BUTTON

    }

    def fill_sign_up_fields(self, first_name, last_name, email, password):
        self.complete_field(loc.FIRST_NAME_FIELD, first_name)
        self.complete_field(loc.LAST_NAME_FIELD, last_name)
        self.complete_field(locs.EMAIL_FIELD, email)
        self.complete_field(locs.PASSWORD_FIELD, password)

    def click_sign_up_button(self):
        self.click_button(loc.SIGN_UP_BUTTON)

    def complete_checkbox(self):
        self.click_button(loc.POLICY_CONFIRM_CHECKBOX)
