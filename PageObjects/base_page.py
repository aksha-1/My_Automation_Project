from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.custome_logger import LogGen
import os 
import time
import datetime

"""
. Use a base class (Optional)
A BasePage can include common functionalities like navigating to a page, 
waiting for elements, and handling alerts.
"""
 # Wrapper for locating an element safely
class BasePage:
    screen_save_file ="Screenshots"
    log=LogGen.log_gen()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        

    def save_screenshot(self, screen_name):

        os.makedirs(self.screen_save_file, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(
            self.screen_save_file,
            f"{screen_name}_{timestamp}.png")

        self.driver.save_screenshot(file_path)

        self.log.info(f"Screenshot saved successfully: {file_path}")

    # Wrapper for locating an element safely
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Wrapper for locating an element safely
    def type(self, locator, text):
        self.wait.until( EC.visibility_of_element_located(locator) ).send_keys(text)

    def get_text(self, locator):
        return self.wait.until( EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def open_url(self, url):
        self.driver.get(url)

# list use of warper 
"""
click(locator)

enter_text(locator, value)

get_text(locator)

is_displayed(locator)

select_dropdown(locator, text)

scroll_to(locator)

js_click(locator)

hover(locator)

drag_and_drop(source, target)

take_screenshot(name)
"""