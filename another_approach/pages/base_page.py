from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import NoSuchElementException, WebDriverException


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_element_visible(self, by, locator):
        try:
            self.wait.until(visibility_of_element_located((by, locator)))
            return True
        except WebDriverException:
            return False


class BasePage(Page):
    pass
    # @property
    # def logo(self):
    #     return self.driver.find_element_by_css_selector("#header > a > img")