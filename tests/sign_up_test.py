import time

import pytest
from pages import sign_up_page


class TestSignUp:

    def test_sign_up(self, setUp):
        page = sign_up_page.SignUpPage(setUp)
        first_name = "Marina"
        last_name = "Zelenskaya"
        email = "osychenkomarina@gmail.com"
        password = "1s5b12z2q"
        time.sleep(1)
        page.fill_sign_up_fields(first_name, last_name, email, password)
        page.complete_checkbox()
        page.click_sign_up_button()


