import unittest
import HTMLTestRunner
import os
import datetime
from ColossusTestCase import ColossusTestCase
# get the directory path to output report file
dir = os.getcwd()
file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M_report.html")

# get all tests from SearchProductTest and HomePageTest class
esnap_tests = unittest.TestLoader().loadTestsFromTestCase(ColossusTestCase)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([esnap_tests])
# open the report file
outfile = open(dir + "/results/" + file_name , "wb")
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
                stream=outfile,
                title='Test Report',
                description='Sample Test'
                )
runner.run(smoke_tests)