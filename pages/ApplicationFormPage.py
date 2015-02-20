__author__ = 'Yunxi Lin'

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from pages.BasePage import BasePage
from locators.ApplicationFormPageLocators import ApplicationFormPageLocators as AFL
#from common.CommonMethods import CommonMethods

class ApplicationFormPage(BasePage):

    def fill_in_default_data(self):
        self.cm.set_value_to_element(self.driver, 'qa@capitalone.com', *AFL.EMAIL)
        self.cm.set_value_to_element(self.driver, '519-776-2012', *AFL.PHONE)
        self.cm.set_value_to_element(self.driver, '23 VICTORIA AVE', *AFL.ADDRESS)
        self.cm.set_value_to_element(self.driver, 'ESSEX', *AFL.CITY)
        self.cm.select_dropdown_by_text(self.driver, 'Ontario', *AFL.STATE)
        self.cm.set_value_to_element(self.driver, 'N8M1M4', *AFL.ZIP)
        self.cm.set_value_to_element(self.driver, '16/05/1962', *AFL.DOB)
        self.cm.select_dropdown_by_text(self.driver, 'Retired', *AFL.EMPLOYMENT_STATUS)
        self.cm.set_value_to_element(self.driver, '888888', *AFL.INCOME)
        self.cm.click(self.driver, *AFL.INCOME_ANNUAL)
        self.cm.click(self.driver, *AFL.CONSENT_CHECKBOX)

    def click_continue(self):
        print('continue')
        self.cm.click(self.driver, *AFL.CONTINUE_BTN)


