from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def current_url (self, browser)
        browser.switch_to_window(browser.window_handles[1])
        current_url = browser.current_url
        return(current_url)
