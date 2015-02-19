__author__ = 'XMB089'

"""
    sample
"""
import unittest
from pages.TestAuthenticateMerchantPage import TestAuthenticateMerchantPage
from selenium.webdriver.common.by import By
from common.CommonMethods import CommonMethods


class ColossusTestCase(unittest.TestCase):

    def setUp(self):
        self.cm = CommonMethods()
        self.cm.open_browser('chrome')
        self.cm.navigate('https://qa2.esnapw.btctest.com/hts/TestAuthenticateMerchant.html')
        self.driver = self.cm.get_driver()

    def test_navigation(self):
        start_page = TestAuthenticateMerchantPage(self.driver)
        print('TMP')
        start_page.select_merchant('00010N')
        start_page.submit_merchant()
        start_page.verify_landing_title()
        assert isinstance(start_page.get_driver, object)
        self.driver = start_page.get_driver()

    def tearDown(self):
        #self.cm.teardown(self.driver)
        self.driver.close()
if __name__ == "__main__":
    unittest.main()

