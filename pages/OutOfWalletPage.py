__author__ = 'Yunxi Lin'
from selenium import webdriver
from locators.OutOfWalletPageLocators import OutOfWalletPageLocators as OOWL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class OutOfWalletPage(BasePage):

    def answer_question_default(self):
        questions = WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'input[name="QuestionIds"]')))
        self.logger.info('%d questions' % len(questions))
        for qs in questions:
            q_ID = qs.get_attribute('value')
            print('Question ' + q_ID)
            ansStr = self.find_correct_answer_default(q_ID)
            answers = self.driver.find_element_by_css_selector('label[for^="' + q_ID + '-"]')
            ansNum = 1
            for ans in answers:
                if(ansNum == len(questions)):
                    self.cm.click(self.driver, By.TAG_NAME,'span')
                    self.logger.info('The last one default answer selected')
                    break
                elif(ansStr is not None):
                    if(ans.get_text().contains(ansStr)):
                        self.cm.click(self.driver, By.TAG_NAME, 'span')
                        self.logger.info(q_ID + ' answer: ' + ans.get_text() + ' is checked')
                        break
            ++ ansNum

    def find_correct_answer_default(self, Id):
        if(Id == '157'):
            return 'NO'
        elif(Id == '162'):
            return 'SEARS'
        elif(Id == '163'):
            return 'TORONTO DOMINION BANK'
        elif(Id == '167'):
            return '52'
        elif(Id == '173'):
            return '2000'
        elif(Id == '175'):
            return 'TORONTO DOMINION BANK'
        elif(Id =='1021'):
            return '270 RAGLAN ST S'
        elif(Id =='1022'):
            return 'NO'
        elif(Id == '2008'):
            return '2000'
        elif(Id == '2030'):
            return '270 RAGLAN ST S'
        elif(Id == '2039'):
            return 'TD - CANADA TRUST, 270 RAGLAN ST S'
        else:
            return None
    def click_submit_btn(self):
        self.cm.click(self.driver,*OOWL.SUBMIT_BTN)