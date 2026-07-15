from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
. Use a base class (Optional)
A BasePage can include common functionalities like navigating to a page, 
waiting for elements, and handling alerts.
"""
class BasePage:
    screen_save_file ="Screenshorts"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def save_screenshort(self,screen_name):
        self.driver.save_screenshot(f"./{self.screen_save_file}/{screen_name}.png")

    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def type(self, locator, text):
        self.wait.until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    def is_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def open_url(self, url):
        self.driver.get(url)