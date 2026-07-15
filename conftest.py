import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key
from  utilities.custome_logger import LogGen
log=LogGen.log_gen()

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
            driver = webdriver.Chrome()
            log.info("************* Launching the chrome browser **************")
    elif browser=="edge":
         driver=webdriver.Edge()
         log.info("************ Launching the edge  browser ******************")
    else:
        raise Exception ("Please provide the browser name e.g. ---browser= 'browser name'")
         
    driver.maximize_window()  
    yield driver
    driver.quit()
    log.info("*******closed the  browser ************* ")


def pytest_addoption(parser): # this will get value from CLI /hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to set up method 
    return request.config.getoption("--browser")

##########  Pytest HTML report ################################
# It is hook adding Environement information into HTML report 
# Hook to add Environment information into HTML report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "PhysicsAI"
    config.stash[metadata_key]["Environment"] = "QA"
    config.stash[metadata_key]["Owner"] = "Akshay"


# Hook to remove/modify Environment information in HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("PLUNGINS", None)