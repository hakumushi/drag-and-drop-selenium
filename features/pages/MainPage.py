from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class MainPage(BasePage):

    URL='https://jqueryui.com/droppable/'

    def open_main_page(self):
        super().open_url(self.URL)
