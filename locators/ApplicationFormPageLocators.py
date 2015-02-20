__author__ = 'Yunxi Lin'

from selenium.webdriver.common.by import By

class ApplicationFormPageLocators():
    EMAIL = (By.ID,'ApplicantEmail')
    PHONE = (By.ID,'ApplicantPrimaryPhone')
    ADDRESS = (By.ID,'ApplicantHomeAddressLine1')
    APT = (By.ID,'ApplicantAptNumber')
    CITY = (By.ID,'ApplicantCity')
    STATE = (By.ID,'ApplicantProvince')
    ZIP = (By.ID,'ApplicantPostalCode')
    DOB = (By.ID,'dob')
    SSN = (By.ID,'ApplicantSSN')
    EMPLOYMENT_STATUS = (By.ID,'ApplicantEmploymentStatus')
    EMPLOYER_NAME = (By.ID,'CanadianApplicantEmployer')
    OCCUPATION = (By.ID,'CanadianApplicantOccupation')
    INCOME = (By.ID,'CanadianApplicantIncome')
    INCOME_WEEKLY = (By.CSS_SELECTOR, 'label[for="WEEK"] span')
    INCOME_MONTHLY = (By.CSS_SELECTOR, 'label[for="MONTH"] span')
    INCOME_ANNUAL = (By.CSS_SELECTOR, 'label[for="YEAR"] span')
    CONSENT_CHECKBOX = (By.CSS_SELECTOR, 'label[for="TermsAndConditionAccept"] span')
    CONTINUE_BTN = (By.ID, 'cmd_ApplicantInfo')

