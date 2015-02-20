__author__ = 'Yunxi Lin'

from pages.BasePage import BasePage
class PendingPage(BasePage):
    def print_display(self):
        self.logger.info('Pending Page Displayed')