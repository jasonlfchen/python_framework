_name_ = 'jason'

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

chromedriver = "/Users/Jason/PycharmProjects/drivers/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
phantomdriver = "/Users/Jason/PycharmProjects/drivers/phantomjs"
#os.environ["webdriver.phantomjs.driver"] = phantomdriver

driver = webdriver.Chrome(chromedriver)
driver.get("https://qa4.ca.capitalonecardservice.btctest.com/ecare/loginform")
print("on eCare site")
assert "Online Account Access Login" in driver.title
elem = driver.find_element_by_id("userid1")
elem.send_keys("CO7748U")
elem = driver.find_element_by_id("password1")
elem.send_keys("COACCOUNT1")
driver.find_element_by_name("button1").click()
print("entered credentials")
assert "Account Overview" in driver.title
print("test passed")
driver.close()
