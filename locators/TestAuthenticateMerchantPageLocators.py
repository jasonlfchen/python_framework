__author__ = 'Yunxi Lin'

from selenium.webdriver.common.by import By

class TestAuthenticateMerchantPageLocators():
    DROP_DOWN_ELEMENT = (By.NAME, 'MerchantNumberSent')
    SUBMIT_BTN = (By.NAME, 'SubmitButton')