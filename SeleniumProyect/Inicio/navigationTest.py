
from controllerDriver import ControllerWindow
import unittest
import time

class ReturnTitle(unittest.TestCase, ControllerWindow):
       
    def star(url):
        controller = ControllerWindow(url)
        controller.aperturaLink()
        print(controller.driver.title)
        time.sleep(2)
        controller.driver.get('https://www.selenium.dev/')
        time.sleep(2)
        #back
        controller.driver.back()
        print(controller.driver.current_url)
        time.sleep(2)
        #forward
        time.sleep(2)
        controller.driver.forward()
        print(controller.driver.current_url)
        #refresh
        time.sleep(2)
        controller.driver.refresh()
        print(controller.driver.current_url)
        time.sleep(2)

    #def test_login(self):
    def tearDown(self):
        self.driver.quit()



ReturnTitle.star('https://www.google.com/')