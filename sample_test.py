_name_ = 'jason'


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://qa4.ca.capitalonecardservice.btctest.com/ecare/loginform")
assert "Online Account Access Login" in driver.title
elem = driver.find_element_by_id("userid1")
elem.send_keys("CO7748U")
elem = driver.find_element_by_id("password1")
elem.send_keys("COACCOUNT1")
driver.find_element_by_name("button1").click()
assert "Account Overview" in driver.title
driver.close()
