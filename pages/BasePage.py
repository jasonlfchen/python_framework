__author__ = 'XMB089'
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from common.CommonMethods import CommonMethods


class BasePage(object):
    """Base page object"""

    implicit_wait = 30

    def __init__(self, driver):#resource_handler
        #self.driver = resource_handler.driver
        #self.resource_handler = resource_handler
        self.driver = driver
        self.cm = CommonMethods()

    def wait_until(self, by, value, timeout=5, parent_element=None):

        if parent_element:
            WebDriverWait(parent_element, timeout).until(
                lambda parent_element: self.is_element_present(by, value, parent_element=parent_element))
        else:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.is_element_present(by, value))

    def is_element_present(self, by, value, parent_element=None):
        self.driver.implicitly_wait(0)
        if parent_element:
            element_or_driver = parent_element
        else:
            element_or_driver = self.driver
        try:
            element_or_driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            self.driver.implicitly_wait(self.implicit_wait)

    def verify_title(self, expected_title):
        wait = WebDriverWait(self.driver, 30)
        decision = wait.until(EC.title_is(expected_title))
        assert expected_title == self.driver.title,'Expected: ' + expected_title + ' ' + 'Actual: ' + self.driver.title

    def get_driver(self):
        return self.driver