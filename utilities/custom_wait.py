from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
1) CustomWait → waiting and synchronization.
2) Return the element when it is ready
advatange :
1) avoide code duplicate 
2) reduce flaky test 
3) easy to maintain and understand 
4) 
"""

class CustomWait:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visibility(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_presence(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_invisible(self, locator):
        return self.wait.until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_title(self, title):
        return self.wait.until(
            EC.title_contains(title)
        )

    def wait_for_url(self, url):
        return self.wait.until(
            EC.url_contains(url)
        )
    
"""
wait_for_visibility()

wait_for_clickable()

wait_for_presence()

wait_for_invisibility()

wait_for_alert()

wait_for_title()

wait_for_url()

wait_for_frame()

wait_for_window_count()
"""