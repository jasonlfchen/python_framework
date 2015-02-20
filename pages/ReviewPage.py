__author__ = 'Yunxi Lin'

from pages.BasePage import BasePage
from locators.ReviewPageLocators import ReviewPageLocators as RPL
class ReviewPage(BasePage):

    def click_submit_btn(self):
        self.cm.click(self.driver,*RPL.SUBMIT_BTN)