import selenium 
from selenium.webdriver.common.by import By
from selenium import webdriver
from PageObjects.base_page import BasePage
class LoginPage(BasePage):

    __textbox_username = (By.XPATH,'//input[contains(@class,"oxd-input")]') #or //input[@name="username"]'#'//input[@name="username"]'
    __textbox_password = (By.XPATH,'//input[@name="password"]')
    __button_login = (By.XPATH,'//button[@type="submit"]')
    __button_logout = (By.LINK_TEXT,'Logout')
    __click_logoout_drop_down = (By.XPATH,'//span[@class="oxd-userdropdown-tab"]//img')
    __message_invalid = (By.XPATH,'//p[text()="Invalid credentials"]')

    def __init__(self,driver): #constructor chaining,Constructor Inheritance
        self.driver=driver
        super().__init__(driver) #Inside the child constructor, super().__init__() calls the Parent constructor.

    def set_username(self,username): # * is used for the unpacking 
        self.driver.find_element(*self.__textbox_username).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(*self.__textbox_password).send_keys(password)

    
    def click_on_logout_button(self):
        self.driver.find_element(*self.__click_logoout_drop_down).click()

    def click_login(self,):
        self.driver.find_element(*self.__button_login).click()

    def click_logout(self):
        self.driver.find_element(*self.__button_logout).click()
    def get_invalid_text(self):
        self.driver.find_element(*self.__message_invalid)
        



