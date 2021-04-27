
from pages import sign_up_page


class TestSignUp:

    def test_sign_up(self, setUp):
        page = sign_up_page.SignUpPage(setUp)
        first_name = "Marina"
        last_name = "Zelenskaya"
        email = "marisabelosy+1@gmail.com"
        password = "mari021292"
        page.fill_sign_up_fields(first_name, last_name, email, password)
        page.complete_checkbox()
        page.click_sign_up_button()
        assert page.check_element_visibility('submit_code_button')








