from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class MainPage(BasePage):

    URL='https://jqueryui.com/droppable/'
    SQUARE = (By.ID, 'draggable')
    BOX = (By.ID, 'droppable')

    def open_main_page(self):
        super().open_url(self.URL)

    def drag_and_drop_the_square_to_the_box(self):
        square = super().find(self.SQUARE)
        box = super().find(self.BOX)
        super().drag_and_drop(square, box)
