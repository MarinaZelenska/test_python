

from pages.base_page import BasePage
from pages.locators import sign_in_locators as loc, base_page_locators as locs


class SignInPage(BasePage):
    CHECK = {
        'user_menu': loc.USER_MENU
    }

    def select_sign_in_tab(self):
        self.click_button(loc.TAB_SIGN_IN)

    def fill_sign_in_fields(self, email, password):
        self.complete_field(locs.EMAIL_FIELD, email)
        self.complete_field(locs.PASSWORD_FIELD, password)

    def click_submit_button(self):
        self.click_button(locs.SUBMIT)
