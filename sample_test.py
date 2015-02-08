_name_ = 'jason'

import pytest
from urlparse import
from selenium import webdriver


BROWSERS = {
    'firefox': DesiredCapabilities.FIREFOX,
    'chrome': DesiredCapabilities.CHROME,
}

WEBDRIVER_ENDPOINT = 'http://localhost:4444/wd/hub'

BASE_URL = 'http://python.org'


class BaseUrlWrapper(webdriver.Remote):
    def __init__(self, base, *args, **kwargs):
            self._base_url = base
            super(BaseUrlWrapper, self).__init__(*args, **kwargs)

    def get(self, url):
        url = urljoin(self._base_url, url)
        return super(HostMappedWrapper, self).get(url)


@pytest.yield_fixture(params=BROWSERS.keys())
def browser(request):
    driver = BaseUrlWrapper(
        base=BASE_URL,
        command_executor=WEBDRIVER_ENDPOINT,
        desired_capabilities=BROWSERS[request.param]
    )
    yield driver
    driver.quit()


def test_homepage(browser):
    browser.get('/')
    assert 'Python' in browser.title

def test_about(browser):
    browser.get('/about/')
    assert 'About Python' in browser.title

def test_other(browser):
    # Absolute URLs still yield the expected result
    browser.get('https://www.ruby-lang.org/en/')
    pytest.fail("Ruby always fails!")
