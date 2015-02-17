__author__ = 'XMB089'

"""
    sample
"""
from CommonMethods import CommonMethods
from selenium.webdriver.common.by import By


cm = CommonMethods()
cm.open_browser('chrome')
cm.navigate('https://qa2.esnapw.btctest.com/hts/TestAuthenticateMerchant.html')
driver = cm.get_driver()
cm.select_dropdown_by_value(driver,By.NAME,'MerchantNumberSent','00010N')
cm.click(By.NAME, 'SubmitButton')

