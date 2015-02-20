_name_ = 'jason'

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from common.CommonMethods import CommonMethods

cm = CommonMethods()
#cm.set_browser_path('chrome','/Users/Jason/PycharmProjects/driver/chromedriver') #on mac
cm.open_browser('firefox')
cm.navigate("https://qa4.ca.capitalonecardservice.btctest.com/ecare/loginform")
print("on eCare site")
cm.assert_title("Online Account Access Login")
driver = cm.get_driver()
#assert "Online Account Access Login" in driver.title
cm.set_value_to_element(driver,'CO7748U','id','userid1')
cm.set_value_to_element(driver,'COACCOUNT1','id','password1')
#elem = driver.find_element_by_id("userid1")
#elem.send_keys("CO7748U")
#elem = driver.find_element_by_id("password1")
#elem.send_keys("COACCOUNT1")
cm.click(driver,'name','button1')
#driver.find_element_by_name("button1").click()
print("entered credentials")
cm.assert_title("Account Overview")
print("test passed")
cm.close_browser()
