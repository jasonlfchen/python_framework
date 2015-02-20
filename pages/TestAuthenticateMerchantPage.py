__author__ = 'Yunxi Lin'

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

#from pages.BasePage import BasePage
from locators.TestAuthenticateMerchantPageLocators import TestAuthenticateMerchantPageLocators
from common.CommonMethods import CommonMethods

class TestAuthenticateMerchantPage(object):#BasePage
    #driver = BasePage.get_driver()
    def __init__(self, driver):
        self.driver = driver
        self.cm = CommonMethods()

    def select_merchant(self, merchant_id):
        self.cm.select_dropdown_by_value(self.driver, merchant_id,*TestAuthenticateMerchantPageLocators.DROP_DOWN_ELEMENT)

    def submit_merchant(self):
        self.cm.click(self.driver, *TestAuthenticateMerchantPageLocators.SUBMIT_BTN)

    def get_driver(self):
        return self.driver