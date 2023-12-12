import uuid

import pytest
from allure_commons.types import AttachmentType

import urls
from UI.pages.registration_page import RegistrationPage
from UI.locators.planning_page_locators import PlanningPageLocators
from UI.locators.registration_page_locators import RegistrationPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import data


@allure.feature('Registration')
@allure.story('Registration with valid email and valid password')
@allure.severity('blocker')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.skip
def test_registration_positive(browser):
    page = RegistrationPage(browser, urls.LINK_REGISTRATION)
    page.open()
    with allure.step('Registration with valid email'):
        page.go_to_reg_first_name()
        page.go_to_reg_last_name()
        page.go_to_reg_business_email()
        page.go_to_reg_organization()
        page.go_to_reg_password()
        page.go_to_reg_checkbox()
        page.go_to_reg_create_org_btn()
        page.go_to_reg_skip_btn()
    with allure.step("Verify user_menu is displayed"):
        user_menu = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(PlanningPageLocators.USER_MENU)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='result' + e, attachment_type=AttachmentType.PNG)

    assert user_menu.is_displayed()


@allure.feature('Registration')
@allure.story('Registration with invalid email and valid password')
@allure.severity('critical')
@pytest.mark.smoke
@pytest.mark.regression
def test_registration_negative_existed_email(browser):
    page = RegistrationPage(browser, urls.LINK_REGISTRATION)
    page.open()
    with allure.step(f'Registration with existed email: {data.existed_email}'):
        page.go_to_reg_first_name()
        page.go_to_reg_last_name()
        business_email = browser.find_element(*RegistrationPageLocators.REG_BUSINESS_EMAIL)
        business_email.clear()
        business_email.send_keys(data.existed_email)
        page.go_to_reg_organization()
        page.go_to_reg_password()
        page.go_to_reg_checkbox()
        page.go_to_reg_create_org_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REG_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='result' + e, attachment_type=AttachmentType.PNG)

    assert error_message.text == ("An account with this email address already exist. "
                                  "Please use another Email OR login to existing one.")


@allure.feature('Registration')
@allure.story('Registration with invalid email and valid password')
@allure.severity('critical')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('email', [data.invalid_email_1, data.invalid_email_2])
def test_registration_negative_email(browser, email):
    page = RegistrationPage(browser, urls.LINK_REGISTRATION)
    page.open()
    with allure.step(f'Registration with invalid email: {email}'):
        page.go_to_reg_first_name()
        page.go_to_reg_last_name()
        business_email = browser.find_element(*RegistrationPageLocators.REG_BUSINESS_EMAIL)
        business_email.clear()
        business_email.send_keys(email)
        page.go_to_reg_organization()
        page.go_to_reg_password()
        page.go_to_reg_checkbox()
        page.go_to_reg_create_org_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REG_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='result' + e, attachment_type=AttachmentType.PNG)

    assert error_message.text == "Email is not valid."


@allure.feature('Registration')
@allure.story('Registration with valid email and invalid password')
@allure.severity('critical')
@pytest.mark.smoke
@pytest.mark.regression
def test_registration_negative_password_not_8_characters(browser):
    page = RegistrationPage(browser, urls.LINK_REGISTRATION)
    page.open()
    with allure.step(f'Registration with invalid password: {data.invalid_password_1}'):
        page.go_to_reg_first_name()
        page.go_to_reg_last_name()
        business_email = browser.find_element(*RegistrationPageLocators.REG_BUSINESS_EMAIL)
        business_email.clear()
        business_email.send_keys(data.not_existed_email)
        page.go_to_reg_organization()
        reg_password = browser.find_element(*RegistrationPageLocators.REG_PASSWORD)
        reg_password.clear()
        reg_password.send_keys(data.invalid_password_1)
        page.go_to_reg_checkbox()
        page.go_to_reg_create_org_btn()
    with allure.step("Verify error message is displayed"):
        error_message = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.REG_ERROR_MESSAGE)
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='result' + e, attachment_type=AttachmentType.PNG)

    assert error_message.text == "Password should contain 8 or more characters"


@allure.feature('Registration')
@allure.story('Registration with valid email and invalid password')
@allure.severity('critical')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize('password', [data.invalid_password_2, data.invalid_password_3])
def test_registration_negative_password(browser, password):
    page = RegistrationPage(browser, urls.LINK_REGISTRATION)
    page.open()
    with allure.step(f'Registration with invalid password: {password}'):
        page.go_to_reg_first_name()
        page.go_to_reg_last_name()
        business_email = browser.find_element(*RegistrationPageLocators.REG_BUSINESS_EMAIL)
        business_email.clear()
        business_email.send_keys(data.not_existed_email)
        page.go_to_reg_organization()
        reg_password = browser.find_element(*RegistrationPageLocators.REG_PASSWORD)
        reg_password.clear()
        reg_password.send_keys(password)
        page.go_to_reg_checkbox()
        page.go_to_reg_create_org_btn()
    with allure.step("Verify error message is displayed"):
        alert = WebDriverWait(browser, 10).until(
            EC.Alert
        )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='result' + e, attachment_type=AttachmentType.PNG)

    assert alert
    alert.accept()
