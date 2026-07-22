import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.custome_logger import LogGen
import os 
print("current working dir",os.getcwd())
import time
class Test_001_login():
    #base_url=ReadConfig.get_application_url()
    # username=ReadConfig.get_username()
    # password =ReadConfig.get_password()
    log=LogGen.log_gen()

    @pytest.mark.smoke
    @pytest.mark.dependency()
    def test_homepage_title(self,setup,config_data,request):
        self.log.info("************ Test_001_login *********************")
        self.log.info("************ verify homepage_title *********************")
        self.driver=setup
        self.log_page = LoginPage(self.driver)
        test_name = request.node.name
        self.driver.get(config_data["base_url"])
        a=self.driver.title
        if a=="OrangeHRM":
            assert True
            self.log.info("************ Home page title test is passed *********************")
        else:
            self.log.error("************ Home page titile test is failed *********************")
            self.log_page.save_screenshot(test_name)
            assert False 


        assert a=="OrangeHRM",f"expected to:'OrangeHRM' actual got :{self.driver.title}{self.driver.save_screenshot(f"{os.path.join(os.path.curdir,'Screenshorts','test_homepage_title.png')}")}"

    @pytest.mark.regression
    def test_login_homepage(self,setup,config_data):
        self.log.info("************ verify test_login_homepage  *********************")
        self.driver = setup
        self.driver.get(config_data["base_url"])
        log_page = LoginPage(self.driver)
        time.sleep(2)
        log_page.set_username(config_data["username"])
        log_page.set_password(config_data["password"])
        log_page.click_login()
        title_1 = self.driver.title
        if title_1 == "OrangeHRM":
            assert True
            self.log.info("************ login test  is passed  *********************")
        else:
            self.log.error("************ login test is failed  *********************")
            assert False 
        
    
    @pytest.mark.dependency(depends=["test_homepage_title"])
    @pytest.mark.smoke
    def test_title(self,setup,config_data):
        self.log.info("************ Test_001_login *********************")
        self.log.info("************ verify homepage_title *********************")
        self.driver=setup
        self.driver.get(config_data["base_url"])
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

    def test_logout(self,setup,config_data):
        self.driver=setup
        self.driver.get(config_data["base_url"])
        log_page=LoginPage(self.driver)
        time.sleep(3)
        log_page.set_username(config_data["username"])
        log_page.set_password(config_data["password"])
        log_page.click_login()
        time.sleep(2)
        print(self.driver.current_url)
        actual_url = self.driver.current_url
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        
        if actual_url!=expected_url:
            self.log.error("*********test login url failed***********************")
        assert actual_url==expected_url ,\
        f"Expected to get {expected_url} but got {actual_url}"
        self.log.info("*********************login test passed *************************")
        time.sleep(3)
        log_page.click_on_logout_button()
        time.sleep(3)
        log_page.click_logout()
        actual_url=self.driver.current_url
        print(self.driver.current_url)
        url_expected="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        if actual_url!=url_expected:
            self.log.error("*********test logout url failed***********************")
        assert actual_url==url_expected ,\
        f"Expected to get {url_expected} but got {actual_url}"
        self.log.info("*********************logout test passed *************************")














