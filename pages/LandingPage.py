__author__ = 'Yunxi Lin'


from pages.BasePage import BasePage
from locators.LandingPageLocators import LandingPageLocators as LPL
class LandingPage(BasePage):

    def fill_in_default(self):
        self.cm.set_value_to_element(self.driver,'caroline',*LPL.PRIMARY_FIRST_NAME)
        self.cm.set_value_to_element(self.driver,'catts',*LPL.PRIMARY_LAST_NAME)
        self.cm.set_value_to_element(self.driver,'613023542312',*LPL.PRIMARY_MEMBER_ID)
        self.cm.click(self.driver,*LPL.ADD_AUTHORIZED_USER_NO)
        self.cm.click(self.driver,*LPL.CONSENT_CHECKBOX)

    def click_submit_btn(self):
        self.cm.click(self.driver,*LPL.SUBMIT_BTN)