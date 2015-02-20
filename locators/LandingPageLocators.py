__author__ = 'Yunxi Lin'

from selenium.webdriver.common.by import By
class LandingPageLocators():
    PRIMARY_FIRST_NAME = (By.NAME,'CanadianApplicantNameFirst')
    PRIMARY_LAST_NAME = (By.NAME,'CanadianApplicantNameLast')
    PRIMARY_MEMBER_ID = (By.NAME,'CanadianMembershipId')
    ADD_AUTHORIZED_USER_YES = (By.CSS_SELECTOR,'label[for="authYes"] span.icon')
    ADD_AUTHORIZED_USER_NO = (By.CSS_SELECTOR,'label[for="authNo"] span.icon')
    CONSENT_CHECKBOX = (By.CSS_SELECTOR,'label.checkbox.icon.icon_check_box span.icon')
    SUBMIT_BTN = (By.ID,'cmd_CanadianSecondLook')

