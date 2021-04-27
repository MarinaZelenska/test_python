from selenium.webdriver.common.by import By

FIRST_NAME_FIELD = (By.XPATH, '//input[@id="first_name"]')
LAST_NAME_FIELD = (By.ID, 'last_name')
EMAIL_FIELD = (By.ID, 'email')
PASSWORD_FIELD = (By.ID, 'password')
POLICY_CONFIRM_CHECKBOX = (By.ID, 'policy_confirm-input')
SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'button[data-id="sign-up-btn"]')
FORM = (By.CLASS_NAME, '.medium-mat-form-field')