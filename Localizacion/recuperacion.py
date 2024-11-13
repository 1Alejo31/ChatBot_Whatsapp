from controllerDriver import ControllerWindow
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains  # Importar ActionChains
import pandas as pd


class Recuoeracion:
    
    def __init__(self, url):
        self.controller = ControllerWindow(url)
        

    def star(self):
        self.controller.aperturaLink()
        time.sleep(2)
    
    def getData(self):
        #validar si el elemento existe
        spinnerElement = self.controller.driver.find_element(By.ID, 'spinner')
        print(spinnerElement.is_displayed())
        time.sleep(2)
        
        #validar si el elemento esta seleccionado checkbox
        updateSataionElement = self.controller.driver.find_element(By.ID, 'updated-station')
        print(updateSataionElement.is_selected())
        time.sleep(2)
        
        #save botton
        daveButton = self.controller.driver.find_element(By.ID, 'save-button')
        
        print(daveButton.tag_name)
        print(daveButton.rect)
        print(daveButton.text)
        print(daveButton.is_enabled())
        print(daveButton.value_of_css_property('background-color'))
        print(daveButton.get_attribute('class'))
        time.sleep(2)
        
    def tearDown(self):
        self.driver.quit()

localization = Recuoeracion('https://courses.academti.com/chatbot/measurements/add')
localization.star()
localization.getData()