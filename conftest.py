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
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser Name: chrome, edge, firefox"
    )

    parser.addoption(
        "--env",
        action="store",
        default="QA",
        help="Environment: DEV, QA, STAGING"
    )



@pytest.fixture()
def browser(request): # This will return the browser value to set up method 
    return request.config.getoption("--browser")

@pytest.fixture()
def env(request):
    return request.config.getoption("--env")


@pytest.fixture(scope="function")
def config_data(env):
    return {
        "base_url": ReadConfig.get_application_url(env),
        "username": ReadConfig.get_username(),
        "password": ReadConfig.get_password()
    }
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


#Database connection 

from Database.db_manager import DBManager
from utilities.readProperties import ReadConfig


@pytest.fixture(scope="session")
def db():

    database = DBManager(
        host=ReadConfig.get_db_host(),
        user=ReadConfig.get_db_user(),
        password=ReadConfig.get_db_password(),
        database=ReadConfig.get_db_name()
    )

    yield database

    database.close()