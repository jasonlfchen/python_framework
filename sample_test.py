_name_ = 'jason'

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from CommonMethods import CommonMethods

cm = CommonMethods()
cm.set_browser_path('chrome','/Users/Jason/PycharmProjects/drivers/chromedriver') #on mac
cm.open_browser('firefox')
cm.navigate("https://qa4.ca.capitalonecardservice.btctest.com/ecare/loginform")
print("on eCare site")
cm.assert_title("Online Account Access Login")
#assert "Online Account Access Login" in driver.title
cm.set_value_to_element('id','userid1','CO7748U')
cm.set_value_to_element('id','password1','COACCOUNT1')
#elem = driver.find_element_by_id("userid1")
#elem.send_keys("CO7748U")
#elem = driver.find_element_by_id("password1")
#elem.send_keys("COACCOUNT1")
cm.click('name','button1')
#driver.find_element_by_name("button1").click()
print("entered credentials")
cm.assert_title("Account Overview")
print("test passed")
cm.close_browser()
