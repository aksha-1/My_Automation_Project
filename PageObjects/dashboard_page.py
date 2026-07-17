from PageObjects.base_page import BasePage
from Components.navigation import Navigation

#inheritance and composition used in your framework
class DashboardPage(BasePage): #inheritance

    def __init__(self, driver):

        super().__init__(driver)

        self.navigation = Navigation(driver) #composition
    def log_out_page(self):
        print(self.navigation.temp()) 