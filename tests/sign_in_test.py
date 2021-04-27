
from pages import sign_in_page


class TestSignIn:

    def test_sign_in(self, setUp):
        page = sign_in_page.SignInPage(setUp)
        email = "marisabelosy@gmail.com"
        password = "mari021292"
        page.select_sign_in_tab()
        page.fill_sign_in_fields(email, password)
        page.click_submit_button()
        assert page.check_element_visibility('user_menu')