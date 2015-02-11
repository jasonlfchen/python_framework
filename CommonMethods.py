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
        self.iePath = 'C:\\selenium\\driver\\IEDriverServer.exe'
        self.chromePath = 'C:\\selenium\\driver\\chromedriver.exe'


    def getUrl(self, baseUrl):
        try:
            appUrl = baseUrl
        except:
            appUrl = 'www.google.com'
            print('URL not found, opening '+ appUrl)
        return appUrl

    def getPage(self, url):
        self.driver.get(url)

    def navigate(self, baseUrl):
        getUrl = self.getUrl(baseUrl)
        try:
            self.getPage(getUrl)
            self.driver.implicitly_wait(10)
        except:
            print('No browser opened')
            self.openBrowser()
            self.getPage(getUrl)
            self.driver.implicitly_wait(10)
            print('URL navigation')

    def openBrowser(self):
        localBrowserName = 'firefox'
        remoteBrowserType = 'firefox'
        platform = 'windows'
        hubUrl = 'localhost:8080'
        os.environ["webdriver.chrome.driver"]=self.chromePath
        os.environ["webdriver.ie.driver"]=self.iePath
        capabilities = DesiredCapabilities
        if(platform!='mac'):
            if(localBrowserName=='firefox'):
                self.driver = webdriver.Firefox()
            elif(localBrowserName=='chrome'):
                self.driver = webdriver.Chrome()
            elif(localBrowserName=='safari'):
                self.driver = webdriver.Safari()
            elif(localBrowserName=='ie'):
                capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
                capabilities['ignoreProtectedModeSettings'] = True
                self.driver = webdriver.Ie(capabilities)
            elif(localBrowserName=='remote'):
                print('Using remote browser')
                if(remoteBrowserType=='firefox'):
                    capabilities = DesiredCapabilities.FIREFOX.copy()
                    capabilities['platform'] = platform
                    capabilities['browserName'] = remoteBrowserType
                    #capabilities['version'] = ''
                    self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=capabilities)
                elif(remoteBrowserType=='ie'):
                    capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
                    capabilities['ignoreProtectedModeSettings'] = True
                    capabilities['platform'] = platform
                    capabilities['browserName'] = remoteBrowserType
                    #capabilities['version'] = ''
                    self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=capabilities)
                elif(remoteBrowserType=='chrome'):
                    capabilities = DesiredCapabilities.CHROME.copy()
                    capabilities['ignoreProtectedModeSettings'] = True
                    capabilities['platform'] = platform
                    capabilities['browserName'] = remoteBrowserType
                    #capabilities['version']
                    self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=capabilities)
                elif(remoteBrowserType=='safari'):
                    capabilities = DesiredCapabilities.SAFARI.copy()
                    capabilities['ignoreProtectedModeSettings'] = True
                    capabilities['platform'] = platform
                    capabilities['browserName'] = remoteBrowserType
                    #capabilities['version']
                    self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=capabilities)
        elif(platform=='mac'):
            if(localBrowserName=='remote'):
                self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=DesiredCapabilities.SAFARI.copy())
                #self.driver =
            else:
                capabilities = DesiredCapabilities.SAFARI.copy()
                self.driver = webdriver.Safari(capabilities)
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def openBrowser(self, remoteBrowserType, localBrowserName, platform, hubUrl):
        os.environ["webdriver.chrome.driver"]=self.chromePath
        os.environ["webdriver.ie.driver"]=self.iePath
        capabilities = DesiredCapabilities
        if(platform!='mac'):
            if(localBrowserName=='firefox'):
                self.driver = webdriver.Firefox()
            elif(localBrowserName=='chrome'):
                self.driver = webdriver.Chrome()
            elif(localBrowserName=='safari'):
                self.driver = webdriver.Safari()
            elif(localBrowserName=='ie'):
                capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
                capabilities['ignoreProtectedModeSettings'] = True
                self.driver = webdriver.Ie(capabilities)
            elif(localBrowserName=='remote'):
                print('Using remote browser')
                if(remoteBrowserType=='firefox'):
                    capabilities = DesiredCapabilities.FIREFOX.copy()
                    capabilities['platform'] = platform
                    capabilities['browserName'] = remoteBrowserType
                    #capabilities['version'] = ''
                    self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=capabilities)
                elif(remoteBrowserType=='ie'):
                    capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
                    capabilities['ignoreProtectedModeSettings'] = True
                    capabilities['platform'] = platform
                    capabilities['browserName'] = remoteBrowserType
                    #capabilities['version'] = ''
                    self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=capabilities)
                elif(remoteBrowserType=='chrome'):
                    capabilities = DesiredCapabilities.CHROME.copy()
                    capabilities['ignoreProtectedModeSettings'] = True
                    capabilities['platform'] = platform
                    capabilities['browserName'] = remoteBrowserType
                    #capabilities['version']
                    self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=capabilities)
                elif(remoteBrowserType=='safari'):
                    capabilities = DesiredCapabilities.SAFARI.copy()
                    capabilities['ignoreProtectedModeSettings'] = True
                    capabilities['platform'] = platform
                    capabilities['browserName'] = remoteBrowserType
                    #capabilities['version']
                    self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=capabilities)
        elif(platform=='mac'):
            if(localBrowserName=='remote'):
                self.driver = webdriver.Remote(command_executor=hubUrl,desired_capabilities=DesiredCapabilities.SAFARI.copy())
                #self.driver =
            else:
                capabilities = DesiredCapabilities.SAFARI.copy()
                self.driver = webdriver.Safari(capabilities)
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def closeBrowser(self, driver):
        try:
            print('Closing browser')
            driver.close()
            print('Browser closed')
        except:
            print('Browser is already closed')

    def tearDown(self, driver):
        print('Closing browser')
        driver.delete_all_cookies()
        driver.quit()
        print('Browser closed')

    def rejectPopUp(self, driver):
        try:
            alert = driver.switch_to.alert
            print('Attempting to dismiss alert')
            alert.dismiss()
            driver.switch_to.default_content()
            print('Alert rejected')
        except:
            print('Alert not found')

    def acceptPopUp(self, driver):
        try:
            alert = self.driver.switch_to.alert
            print('Attempting to accept alert')
            alert.accept()
            self.driver.switch_to.default_content()
            print('Alert accepted')
        except:
            print('Alert not found')


    def sendKeys(self, driver, enterText):
        try:
            alert = self.driver.switch_to.alert
            print('Attempting to send keys to alert')
            alert.send_keys(enterText)
            print('Successfully entered ' + enterText + ' into alert')
        except:
            print('Alert not found')

    def setValue(self, driver, by, byValue, sValue):
        try:
            sLocator = self.driver.find_element(by, byValue)
            elementName = self.driver.find_element(by, byValue).get_attribute('name')
            sLocator.send_keys(sValue)
            print(sValue + ' entered')
        except NoSuchElementException:
            print('Element not found')


