import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions, chrome

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):
    if request.param == "chrome":
     driver = webdriver.Chrome()
    if request.param == "firefox":
        driver= webdriver.Firefox()

    driver.get("https://mytrips.travelsecurity.com/Login.aspx")
    driver.maximize_window()
    yield driver
    driver.quit