# # Dashboard, PIM, Admin, Logout
from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
# # Reusable navigation component

from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage


class Navigation(BasePage):

    dashboard_menu = (By.XPATH, "//span[text()='Dashboard']")
    pim_menu = (By.XPATH, "//span[text()='PIM']")
    leave_menu = (By.XPATH, "//span[text()='Leave']")
    admin_menu = (By.XPATH, "//span[text()='Admin']")
    logout_link = (By.XPATH, "//a[text()='Logout']")


    
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    def open_dashboard(self):
        self.click(self.dashboard_menu)

    def open_pim(self):
        self.click(self.pim_menu)

    def open_leave(self):
        self.click(self.leave_menu)

    def open_admin(self):
        self.click(self.admin_menu)

    def logout(self):
        self.click(self.logout_link)
    def temp(self):
        print("jsut fo check")
"""
Create one when the navigation bar:

Appears on every page
Uses the same locators
Provides common navigation actions

Examples:

Dashboard
Employee
Admin
Reports
Logout
"""