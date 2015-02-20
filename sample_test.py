_name_ = 'jason'

import os

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




logging.config.fileConfig('logging.ini')
logger = logging.getLogger('fileLog')
cm = CommonMethods()
#cm.set_browser_path('chrome','/Users/Jason/PycharmProjects/driver/chromedriver') #on mac
cm.open_browser('phantomjs')
cm.navigate("https://qa4.ca.capitalonecardservice.btctest.com/ecare/loginform")
logger.info("on eCare site")
cm.assert_title("Online Account Access Login")
driver = cm.get_driver()
cm.set_value_to_element(driver,'CO7748U',*usr_name_field)
cm.set_value_to_element(driver,'COACCOUNT1',*password_field)
cm.click(driver,*login_btn)
logger.info("entered credentials")
cm.assert_title("Account Overview")
logger.info("test passed")
cm.close_browser()

