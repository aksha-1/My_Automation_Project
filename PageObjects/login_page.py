import selenium 
from selenium.webdriver.common.by import By
from selenium import webdriver
from PageObjects.base_page import BasePage
class LoginPage(BasePage):

    textbox_username = (By.XPATH,'//input[contains(@class,"oxd-input")]') #or //input[@name="username"]'#'//input[@name="username"]'
    textbox_password = (By.XPATH,'//input[@name="password"]')
    button_login = (By.XPATH,'//button[@type="submit"]')
    button_logout = (By.LINK_TEXT,'Logout')
    click_logoout_drop_down = (By.XPATH,'//span[@class="oxd-userdropdown-tab"]//img')
    message_invalid = (By.XPATH,'//p[text()="Invalid credentials"]')

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    def set_username(self,username):
        self.driver.find_element(self.textbox_username).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(self.textbox_password).send_keys(password)

    
    def click_on_logout_button(self):
        self.driver.find_element(self.click_logoout_drop_down).click()

    def click_login(self,):
        self.driver.find_element(self.button_login).click()

    def click_logout(self):
        self.driver.find_element(self.button_logout).click()
    def get_invalid_text(self):
        self.driver.find_element(self.message_invalid)
        



