from controllerDriver import ControllerWindow
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains  # Importar ActionChains

class Localization:

    def __init__(self, url):
        self.controller = ControllerWindow(url)
        

    def star(self):
        self.controller.aperturaLink()
        time.sleep(2)
        
    def insertData(self, data):
        self.controller.driver.find_element(By.ID, 'stationId').send_keys(data['ID'])
        self.controller.driver.find_element(By.NAME, 'stationName').send_keys(data['Station Name'])
        self.controller.driver.find_element(By.ID, 'elevation').send_keys(data['Elev-m'])
        self.controller.driver.find_elements(By.CLASS_NAME, 'coordinate')[0].send_keys(str(data['Lat']))
        self.controller.driver.find_elements(By.CLASS_NAME, 'coordinate')[1].send_keys(str(data['Lon']))
        stationType = self.controller.driver.find_elements(By.CLASS_NAME, 'form-check-input')
        if data['Type'] == 'Automatic':
            stationType = stationType[0]
        if data['Type'] == 'Semiautomatic':
            stationType = stationType[1]
        if data['Type'] == 'Manual':
            stationType = stationType[2]
        stationType.click()
        time.sleep(1)
        #Generando scroll
        footer = self.controller.driver.find_element(By.TAG_NAME, 'footer')
        ActionChains(self.controller.driver)\
                .scroll_to_element(footer)\
                .perform()
        
        if data['Temperature'] == 1:
            self.controller.driver.find_element(By.NAME, 'temperature').click()
        if data['Atmospheric_Pressure'] == 1:
            self.controller.driver.find_element(By.NAME, 'atmosphericPressure').click()
        if data['Humidity'] == 1:
            self.controller.driver.find_element(By.NAME, 'humidity').click()
        if data['Precipitation'] == 1:
            self.controller.driver.find_element(By.NAME, 'precipitation').click()
        if data['Radiation'] == 1:
            self.controller.driver.find_element(By.NAME, 'radiation').click()
        time.sleep(1)
        self.controller.driver.find_element(By.ID, 'stationId').send_keys('C:\\Users\\alejo\\OneDrive\\Imágenes\\Capturas de pantalla\\Captura de pantalla 2024-06-21 090927.png')
        time.sleep(2)
        
        self.controller.driver.find_element(By.TAG_NAME, 'form').submit()
        time.sleep(5)
        
        #Buscar de manera parcial en un objeto el texto
        self.controller.driver.find_element(By.LINK_TEXT, 'Descargar archivo').click()
        time.sleep(2)
        self.controller.driver.find_element(By.LINK_TEXT, '<< Regresar').click()
        time.sleep(5)
        
    def tearDown(self):
        self.driver.quit()

station_row = {
    'ID':'ACW00011604',   
    'Station Name':'SAVE',
    'Elev-m': 18,
    'Lat': 57.7667,
    'Lon': 11.8667,
    'Type': 'Automatic',
    'Temperature': 1,
    'Atmospheric_Pressure': 1,
    'Humidity': 1,
    'Precipitation': 0,
    'Radiation': 0
}
localization = Localization('http://courses.academti.com/chatbot/weather-stations/add')
localization.star()
localization.insertData(station_row)