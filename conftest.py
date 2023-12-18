import pytest
from selenium import webdriver

import urls
from UI.locators.login_page_locators import LoginPageLocators
from UI.pages.login_page import LoginPage
from UI.locators.planning_page_locators import PlanningPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller


# @pytest.fixture(autouse=True)
# def browser():
#     browser = webdriver.Chrome()
#     yield browser
#     browser.quit()

@pytest.fixture(autouse=True)
def browser():
    chromedriver_autoinstaller.install()
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture()
def login(browser):
    page = LoginPage(browser, urls.LINK_LOGIN)
    page.open()
    page.go_to_login_email()
    page.go_to_login_password()
    page.go_to_login_btn()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(PlanningPageLocators.USER_MENU)
    )


# @pytest.fixture()
# def login(browser):
#     page = LoginPage(browser, urls.LINK_LOGIN)
#     page.open()
#     login_email = browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
#     login_email.clear()
#     login_email.send_keys("lena.postrash@gmail.com")
#     login_password = browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
#     login_password.clear()
#     login_password.send_keys("Mynameislena1!")
#     page.go_to_login_btn()
#     WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located(PlanningPageLocators.USER_MENU)
#     )
