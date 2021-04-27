import pytest
from selenium import webdriver

BASE_URL = 'https://eos.com/crop-monitoring/'



@pytest.fixture(scope='function')
def setUp():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.set_window_size(1980, 1024)
