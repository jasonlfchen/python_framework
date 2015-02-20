__author__ = 'Yunxi Lin'

"""
    sample
"""
import unittest
import logging
import logging.config
from pages.TestAuthenticateMerchantPage import TestAuthenticateMerchantPage
from pages.LandingPage import LandingPage
from pages.ApplicationFormPage import ApplicationFormPage
from pages.ReviewPage import ReviewPage
from pages.OutOfWalletPage import OutOfWalletPage
from pages.ApprovalPage import ApprovalPage
from pages.PendingPage import PendingPage
from selenium.webdriver.common.by import By
from common.CommonMethods import CommonMethods


class ColossusTestCase(unittest.TestCase):

    def setUp(self):
        self.cm = CommonMethods()
        self.cm.open_browser('chrome')
        self.cm.navigate('https://qa2.esnapw.btctest.com/hts/TestAuthenticateMerchant.html')
        self.driver = self.cm.get_driver()
        logging.config.fileConfig('logging.ini')
        self.logger = logging.getLogger('fileLog')

    def test_flow(self):
        start_page = TestAuthenticateMerchantPage(self.driver)
        self.logger.info('Test Authenticate Merchant Page')
        start_page.select_merchant('00010N')
        start_page.submit_merchant()
        self.driver = start_page.get_driver()
        landing_page = LandingPage(self.driver)
        self.logger.info('Landing page')
        landing_page.verify_title('Capital One Canada Credit Card Application: Membership Verification')
        landing_page.fill_in_default()
        landing_page.click_submit_btn()

        self.driver = landing_page.get_driver()
        assert 'Capital One Canada Credit Card Application: Membership Processing' in self.driver.title
        application_page = ApplicationFormPage(self.driver)
        self.logger.info('Application Form Page')
        application_page.fill_in_default_data()
        application_page.verify_title('Capital One Canada Credit Card Application: Data Entry')
        application_page.click_continue()

        self.driver = application_page.get_driver()
        review_page = ReviewPage(self.driver)
        self.logger.info('Review Page')
        review_page.verify_title('Capital One Canada Credit Card Application: Review and Submit')
        review_page.click_submit_btn()

        self.driver = review_page.get_driver()
        try:
            out_of_wallet_page = OutOfWalletPage(self.driver)
            self.logger.info('OOW Page')
            out_of_wallet_page.answer_question_default()
            out_of_wallet_page.verify_title('Capital One Canada Credit Card Application: Verify Your Identity')
            out_of_wallet_page.click_submit_btn()
            self.driver = out_of_wallet_page.get_driver()
        except:
            self.logger.info('OOW not displayed')

        try:
            approval_page = ApprovalPage(self.driver)
            approval_page.verify_title('Capital One Canada Credit Card Application: Approved')
            approval_page.print()
            self.driver = approval_page.get_driver()
        except:
            pending_page = PendingPage(self.driver)
            pending_page.verify_title('Capital One Canada Credit Card Application: Pending')
            pending_page.print()
            self.driver = pending_page.get_driver()



    def tearDown(self):
        #self.cm.teardown(self.driver)
        self.driver.close()
if __name__ == "__main__":
    unittest.main()

