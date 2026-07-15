# @pytest.mark.e2e
# def test_employee_lifecycle(self, setup):

#     self.driver = setup

#     login = LoginPage(self.driver)
#     employee = EmployeePage(self.driver)

#     # Login
#     login.login("Admin", "admin123")

#     # Add Employee
#     employee.add_employee("John", "Doe")

#     # Search Employee
#     employee.search_employee("John Doe")

#     # Delete Employee
#     employee.delete_employee("John Doe")

#     # Logout
#     login.logout()

import pytest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.custome_logger import LogGen

import time
class Test_login_e_to_e:
    base_url=ReadConfig.get_application_url()
    username=ReadConfig.get_username()
    password =ReadConfig.get_password()
    log=LogGen.log_gen()
    
    @pytest.mark.e2e
    @pytest.mark.smoke
    def test_homepage_title1(self,setup,request):
        self.log.info("************ Test_001_login *********************")
        self.log.info("************ verify homepage_title *********************")
        self.driver=setup
        self.pg=LoginPage(self.driver)
        self.pg.open_url(self.base_url)
        a=self.driver.title
        test_name = request.node.name
        if a=="OrangeHR":
            assert True
            self.log.info("************ Home page title test is passed *********************")
        else:
            self.log.error("************ Home page titile test is failed *********************")
            self.pg.save_screenshot(test_name)
            assert False 


        assert a=="OrangeHRM",f"expected to:'OrangeHRM' actual got :{self.driver.title}{self.driver.save_screenshot(f"{os.path.join(os.path.curdir,'Screenshorts','test_homepage_title.png')}")}"
