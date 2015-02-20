_name_ = 'jason'

import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.CommonMethods import CommonMethods
import logging
import logging.config

login_btn = ['name','button1']
usr_name_field = [By.ID,'userid1']
password_field = ['id','password1']

class EcareTests(unittest.TestCase):

    def set_Up(self):
        self.logging.config.fileConfig('logging.ini')
        self.logger = logging.getLogger('fileLog')
        self.cm = CommonMethods()
        #cm.set_browser_path('chrome','/Users/Jason/PycharmProjects/driver/chromedriver') #on mac
        self.cm.open_browser('firefox')
        self.cm.navigate("https://qa4.ca.capitalonecardservice.btctest.com/ecare/loginform")
        self.logger.info("on eCare site")
        self.cm.assert_title("Online Account Access Login")

    def login_test(self):
        self.driver = self.cm.get_driver()
        self.cm.set_value_to_element('CO7748U',*usr_name_field)
        self.cm.set_value_to_element('COACCOUNT1',*password_field)
        self.cm.click(driver,*login_btn)
        self.logger.info("entered credentials")
        self.cm.assert_title("Account Overview")
        self.logger.info("test passed")

    def tear_down(self):
        self.cm.close_browser()

if __name__ == "__main__":
    unittest.main()
