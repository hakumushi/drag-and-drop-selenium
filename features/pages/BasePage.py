from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find(self, locator):
        element = self.wait_for(EC.visibility_of_element_located(locator))
        return element

    def drag_and_drop(self, element, target):
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def wait_for(self,condition, seconds = 5):
        return  WebDriverWait(self.driver,seconds).until(condition)

    def select_a_frame(self, locator):
        element = self.wait_for(EC.visibility_of_element_located(locator))
        self.driver.switch_to_frame(element)
