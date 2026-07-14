import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.custome_logger import LogGen

import time
class Test_001_login:
    base_url=ReadConfig.get_application_url()
    username=ReadConfig.get_username()
    password =ReadConfig.get_password()
    log=LogGen.log_gen()

    @pytest.mark.smoke
    @pytest.mark.dependency()
    def test_homepage_title(self,setup):
        self.log.info("************ Test_001_login *********************")
        self.log.info("************ verify homepage_title *********************")
        self.driver=setup
        self.driver.get(self.base_url)
        a=self.driver.title
        if a=="OrangeHR":
            assert True
            self.log.info("************ Home page title test is passed *********************")
        else:
            self.log.error("************ Home page titile test is failed *********************")
            self.driver.save_screenshot(f"./Screenshorts/test_homepage_title.png")
            assert False 


        assert a=="OrangeHRM",f"expected to:'OrangeHRM' actual got :{self.driver.title}{self.driver.save_screenshot(f"{os.path.join(os.path.curdir,'Screenshorts','test_homepage_title.png')}")}"

    @pytest.mark.regression
    def test_login_homepage(self,setup):
        self.log.info("************ verify test_login_homepage  *********************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.log_page = LoginPage(self.driver)
        time.sleep(2)
        self.log_page.set_username(self.username)
        self.log_page.set_password(self.password)
        self.log_page.click_login()
        title_1 = self.driver.title
        if title_1 == "OrangeHRM":
            assert True
            self.log.info("************ login test  is passed  *********************")
        else:
            self.log.error("************ login test is failed  *********************")
            assert False 
        
    
    @pytest.mark.dependency(depends=["test_homepage_title"])
    @pytest.mark.smoke
    def test_title(self,setup):
        self.log.info("************ Test_001_login *********************")
        self.log.info("************ verify homepage_title *********************")
        self.driver=setup
        self.driver.get(self.base_url)
        a=self.driver.title
        if a=="OrangeHR":
            assert True
            self.log.info("************ Home page title test is passed *********************")
        else:
            self.log.error("************ Home page titile test is failed *********************")
            assert False  
    # def test_logout(self,setup):
    #     self.log.info("************ Verify the logout *********************")  
    #     self.driver=setup
    #     self.driver.get(self.base_url)

    def test_logout(self,setup):
        self.driver=setup
        self.driver.get(self.base_url)
        log_page=LoginPage(self.driver)
        time.sleep(10)
        log_page.set_username(self.username)
        log_page.set_password(self.password)
        log_page.click_login()
        url=self.driver.current_url
        actual="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        if url!=actual:
            self.log.error("*********test login url failed***********************")
        assert url!=actual ,\
        "Expected to get {url} but got {actual}"
        self.log.info("*********************login test passed *************************")
        log_page.click_on_logout_button()
        log_page.click_logout()
        url=self.driver.current_url
        url_expected="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        if url!=url_expected:
            self.log.error("*********test logout url failed***********************")
        assert url!=actual ,\
        "Expected to get {url} but got {actual}"
        self.log.info("*********************logout test passed *************************")














