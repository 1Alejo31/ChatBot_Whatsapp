from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

class ControllerWindow:

    def __init__(self, link):
        self.link = link
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        service = ChromeService(executable_path=r'C:\dchrome\chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def aperturaLink(self):
        self.driver.implicitly_wait(10)
        screen_width = self.driver.execute_script("return window.screen.width;")
        screen_height = self.driver.execute_script("return window.screen.height;")
        window_width = screen_width // 2
        window_height = screen_height
        self.driver.set_window_size(window_width, window_height)
        self.driver.set_window_position(0, 0)
        #self.driver.maximize_window()
        return self.driver.get(self.link)