import selenium 
from selenium.webdriver.common.by import By
from selenium import webdriver
class LoginPage:
    textbox_username_xpath ='//input[contains(@class,"oxd-input")]' #or //input[@name="username"]'#'//input[@name="username"]'
    textbox_password_xpath ='//input[@name="password"]'
    button_login_xpath='//button[@type="submit"]'
    button_logout_linktext='Logout'
    click_logoout_drop_down_xpath='//span[@class="oxd-userdropdown-tab"]//img'
    message_invalid_xpath='//p[text()="Invalid credentials"]'
    def __init__(self,driver):
        self.driver=driver
    def set_username(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

        pass
    def set_password(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    
    def click_on_logout_button(self):
        self.driver.find_element(By.XPATH,self.click_logoout_drop_down_xpath).click()

    def click_login(self,):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT,self.button_logout_linktext).click()
    def get_invalid_text(self):
        self.driver.find_element(By.XPATH,self.message_invalid_xpath)
        



