from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture()
def setup():
    serv_obj = Service("C:/Users/DELL/Downloads/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    return driver

def pytest_configure(config):
    config._metadata['Project Name']='nopCommerce'
    config._metadata['Module Name']='Customer'
    config._metadata['Tester']='Deepak'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugine",None)

