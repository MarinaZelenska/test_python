from selenium.webdriver.common.by import By

FIRST_NAME_FIELD = (By.ID, 'first_name')
LAST_NAME_FIELD = (By.ID, 'last_name')
POLICY_CONFIRM_CHECKBOX = (By.CSS_SELECTOR, 'label[for="policy_confirm-input"]')
SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'button[data-id="sign-up-btn"]')
CONFIRM_CODE_INPUT = (By.ID, 'confirm-code-input')
SUBMIT_CODE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')



