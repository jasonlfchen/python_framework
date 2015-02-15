__author__ = 'Yunxi Lin'
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class CommonMethods():

    def __init__(self):
        self.driver = webdriver
        self.ie_path = 'C:\\selenium\\driver\\IEDriverServer.exe'
        self.chrome_path = 'C:\\selenium\\driver\\chromedriver.exe'
        self.safari_path = ''

    """
        navigation
    """
    def get_url(self, base_url):
        try:
            app_url = base_url
        except:
            app_url = 'www.google.com'
            print('URL not found, opening '+ app_url)
        return app_url

    def get_page(self, url):
        self.driver.get(url)

    def navigate(self, base_url):
        get_url = self.get_url(base_url)
        try:
            self.get_page(get_url)
            self.driver.implicitly_wait(10)
        except:
            print('No browser opened')
            self.open_browser()
            self.get_page(get_url)
            self.driver.implicitly_wait(10)
            print('URL navigation')

    """
        browser control
    """
    def set_browser_path(self,browser_name,browser_path):
        if(browser_name == 'chrome'):
            self.chrome_path = browser_path
        elif(browser_name == 'ie'):
            self.ie_path = browser_path
        elif(browser_name == 'safari'):
            self.safari_path = browser_path


    def open_browser(self, remote_browser_type = 'firefox', local_browser_name = 'firefox',
                     version = '37', hub_url = 'http://localhost:5555/wd/hub'):

        if(local_browser_name == 'chrome'):
            os.environ['webdriver.chrome.driver']=self.chrome_path
        elif(local_browser_name == 'ie'):
            os.environ['webdriver.ie.driver']=self.ie_path
        elif(local_browser_name == 'safari'):
            os.environ['webdriver.safari.driver']=self.ie_path
            os.environ['webdriver.safari.noinstall']=True

        capabilities = DesiredCapabilities

        if(local_browser_name=='firefox'):
            self.driver = webdriver.Firefox()
        elif(local_browser_name=='chrome'):
            self.driver = webdriver.Chrome(self.chrome_path)
        elif(local_browser_name=='safari'):
            self.driver = webdriver.Safari(self.safari_path)
        elif(local_browser_name=='ie'):
            #capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
            #capabilities['ignoreProtectedModeSettings'] = True
            self.driver = webdriver.Ie(self.ie_path)
        elif(local_browser_name=='remote'):
            print('Using remote browser')
            if(remote_browser_type=='firefox'):
                capabilities = DesiredCapabilities.FIREFOX.copy()
                self.driver = webdriver.Remote(command_executor=hub_url,desired_capabilities=capabilities)
            elif(remote_browser_type=='ie'):
                capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
                capabilities['ignoreProtectedModeSettings'] = True
                #capabilities['platform'] = platform
                capabilities['browserName'] = remote_browser_type
                capabilities['version'] = version
                self.driver = webdriver.Remote(command_executor=hub_url,desired_capabilities=capabilities)
            elif(remote_browser_type=='chrome'):
                capabilities = DesiredCapabilities.CHROME.copy()
                #capabilities['platform'] = platform
                capabilities['browserName'] = remote_browser_type
                capabilities['version'] = version
                self.driver = webdriver.Remote(command_executor=hub_url,desired_capabilities=capabilities)
            elif(remote_browser_type=='safari'):
                capabilities = DesiredCapabilities.SAFARI.copy()
                capabilities['ignoreProtectedModeSettings'] = True
                #capabilities['platform'] = platform
                capabilities['browserName'] = remote_browser_type
                capabilities['version'] = version
                self.driver = webdriver.Remote(command_executor=hub_url,desired_capabilities=capabilities)

        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def close_browser(self, driver):
        try:
            print('Closing browser')
            driver.close()
            print('Browser closed')
        except:
            print('Browser is already closed')

    def teardown(self, driver):
        print('Closing browser')
        driver.delete_all_cookies()
        driver.quit()
        print('Browser closed')


    """
        popup handle
    """
    def reject_popup(self, driver):
        try:
            alert = driver.switch_to.alert
            print('Attempting to dismiss alert')
            alert.dismiss()
            driver.switch_to.default_content()
            print('Alert rejected')
        except:
            print('Alert not found')

    def accept_popup(self, driver):
        try:
            alert = self.driver.switch_to.alert
            print('Attempting to accept alert')
            alert.accept()
            self.driver.switch_to.default_content()
            print('Alert accepted')
        except:
            print('Alert not found')


    def send_keys_to_alert(self, driver, enter_text):
        try:
            alert = self.driver.switch_to.alert
            print('Attempting to send keys to alert')
            alert.send_keys(enter_text)
            print('Successfully entered ' + enter_text + ' into alert')
        except:
            print('Alert not found')


    """
        element handle
    """
    def set_value_to_element(self, driver, by, by_value, string_value):
        try:
            string_locator = self.driver.find_element(by, by_value)
            element_name = self.driver.find_element(by, by_value).get_attribute('name')
            string_locator.send_keys(string_value)
            print(string_value + ' entered')
        except NoSuchElementException:
            print('Element ' +  element_name + ' not found')


