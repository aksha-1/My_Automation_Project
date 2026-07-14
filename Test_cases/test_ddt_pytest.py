import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.custome_logger import LogGen
from utilities.exce_utility import DDT

import time
class Test_001_login:
    base_url=ReadConfig.get_application_url()
    log=LogGen.log_gen()
    excel_data=DDT.get_login_data()
    
    @pytest.mark.regression
    @pytest.mark.parametrize("username,password,result",[('Admin','admin123','Pass'),('admin','test','Fail'),('ADMIN','TEST','Fail')])
    def test_login_ddt(self,setup,username,password,result):
        self.log.info("************ verify test_login_homepage  *********************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.log_page = LoginPage(self.driver)
        time.sleep(2)
        self.log_page.set_username(username)
        self.log_page.set_password(password)
        self.log_page.click_login()

        time.sleep(2)
        url=self.driver.current_url  
        title_1 = self.driver.title

        if url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
            assert True
            self.log.info("************ login test  is passed  *********************")
        else:
            self.log.error("************ login test is failed  *********************")
            assert False 
    @pytest.mark.regression
    @pytest.mark.parametrize("username,password,expected",DDT.get_login_data())
    def test_login_excel_ddt(self,setup,username,password,expected):
        self.log.info("************ verify test_login_homepage DDT excel  *********************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.log_page = LoginPage(self.driver)
        time.sleep(2)
        self.log_page.set_username(username)
        self.log_page.set_password(password)
        self.log_page.click_login()

        time.sleep(2)
        url=self.driver.current_url  
        dashboard_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        actula = ("Pass" if url == dashboard_url else "Fail")
        if expected != actula:
            self.log.error("************ Login Test Failed ************")
            self.driver.save_screenshot(f"./Screenshorts/{username}.png")
        assert expected == actula, f"Expected={expected}, Actual={actula}"
        self.log.info("************ Login Test Passed ************")
        