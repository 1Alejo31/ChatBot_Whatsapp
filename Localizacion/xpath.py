from controllerDriver import ControllerWindow
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains  # Importar ActionChains
import pandas as pd

class getXpath:
    def __init__(self, url):
        self.controller = ControllerWindow(url)
        
    def locationXpath(self):
        elementId = self.controller.driver.find_element(getXpath, '//*[@id="sel-country"]')

    def star(self):
        self.controller.aperturaLink()
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

localization = getXpath('https://courses.academti.com/chatbot/measurements/add')
localization.star()
localization.getData()