import time
import uuid

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait

import data
import urls
from UI.locators.planning_page_locators import PlanningPageLocators
from UI.pages.planning_page import PlanningPage


@allure.feature('Add user')
@allure.story('Add user with valid data')
@allure.severity('major')
@pytest.mark.regression
def test_add_user_positive_gigo_team(browser, login):
    e = str(uuid.uuid4().clock_seq)
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_gigo_team()
    page.go_to_add_user()
    page.go_to_select_user_field()
    create_new_user = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(PlanningPageLocators.CREATE_NEW_USER)
    )
    users_before = len(browser.find_elements(*PlanningPageLocators.USER_AVATAR))
    create_new_user.click()
    with allure.step('Enter the data'):
        user_first_name = browser.find_element(*PlanningPageLocators.FIRST_NAME)
        user_first_name.send_keys(e + data.valid_first_name_of_user)
        page.go_to_user_last_name()
        user_email = browser.find_element(*PlanningPageLocators.EMAIL)
        user_email.send_keys(e + data.valid_email_user)
        page.go_to_user_phone_number()
        page.go_to_user_role()
        page.go_to_user__choose_gigo_team()
        page.go_to_user_save_btn()
        time.sleep(2)
    with allure.step("Verify user_avatar is displayed"):
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(PlanningPageLocators.USER_AVATAR)
        )
    users_after = len(browser.find_elements(*PlanningPageLocators.USER_AVATAR))
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='result' + e, attachment_type=AttachmentType.PNG)
    assert users_after == users_before + 1


@allure.feature('Add user')
@allure.story('Add user with valid data')
@allure.severity('major')
@pytest.mark.regression
def test_add_user_positive_qa_learning_team(browser, login):
    e = str(uuid.uuid4().clock_seq)
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_qa_learning_team()
    page.go_to_add_user()
    page.go_to_select_user_field()
    create_new_user = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(PlanningPageLocators.CREATE_NEW_USER)
    )
    users_before = len(browser.find_elements(*PlanningPageLocators.USER_AVATAR))
    create_new_user.click()
    with allure.step('Enter the data'):
        user_first_name = browser.find_element(*PlanningPageLocators.FIRST_NAME)
        user_first_name.send_keys(e + data.valid_first_name_of_user)
        page.go_to_user_last_name()
        user_email = browser.find_element(*PlanningPageLocators.EMAIL)
        user_email.send_keys(e + data.valid_email_user)
        page.go_to_user_phone_number()
        page.go_to_user_role()
        page.go_to_user_choose_qa_learning_team()
        page.go_to_user_save_btn()
        time.sleep(2)
    with allure.step("Verify user_avatar is displayed"):
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(PlanningPageLocators.USER_AVATAR)
        )
    users_after = len(browser.find_elements(*PlanningPageLocators.USER_AVATAR))
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='result' + e, attachment_type=AttachmentType.PNG)
    assert users_after == users_before + 1


@allure.feature('Add user')
@allure.story('Add user with the same name of existed user')
@allure.severity('major')
@pytest.mark.regression
def test_add_user_negative_the_same_name(browser, login):
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_add_user()
    page.go_to_select_user_field()
    create_new_user = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(PlanningPageLocators.CREATE_NEW_USER)
    )
    with allure.step('Enter the data'):
        create_new_user.click()
        page.go_to_user_first_name()
        page.go_to_user_last_name()
        page.go_to_user_email()
        page.go_to_user_phone_number()
        page.go_to_user_role()
        page.go_to_user_save_btn()
        with allure.step('Verify the error message is displayed'):
            error_message = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(PlanningPageLocators.ERROR_MESSAGE_USER_NAME)
            )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='result' + e, attachment_type=AttachmentType.PNG)
    assert error_message.text == "User with this name already exists."


@allure.feature('Add user')
@allure.story('Add user with the same email of existed user')
@allure.severity('major')
@pytest.mark.regression
def test_add_user_negative_the_same_email(browser, login):
    e = str(uuid.uuid4().clock_seq)
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_add_user()
    page.go_to_select_user_field()
    create_new_user = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(PlanningPageLocators.CREATE_NEW_USER)
    )
    create_new_user.click()
    with allure.step('Enter the data'):
        user_first_name = browser.find_element(*PlanningPageLocators.FIRST_NAME)
        user_first_name.send_keys(e + data.valid_first_name_of_user)
        page.go_to_user_last_name()
        user_email = browser.find_element(*PlanningPageLocators.EMAIL)
        user_email.send_keys(data.existed_email)
        page.go_to_user_phone_number()
        page.go_to_user_role()
        page.go_to_user_save_btn()
        with allure.step('Verify the error message is displayed'):
            error_message = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located(PlanningPageLocators.ERROR_MESSAGE_USER_EMAIL)
            )
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name='result' + e, attachment_type=AttachmentType.PNG)
    assert error_message.text == "This email is already taken!"


@allure.feature('Add new team')
@allure.severity('critical')
@pytest.mark.regression
def test_add_new_team_positive(browser, login):
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_manage_team()
    quantity_of_teams_before_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    page.go_to_new_team()
    with allure.step('Enter the name of team'):
        page.go_to_team_name_field()
        page.go_to_create_team_btn()
    quantity_of_teams_after_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name="result" + e, attachment_type=AttachmentType.PNG)
    assert quantity_of_teams_after_creation == quantity_of_teams_before_creation + 1


@allure.feature('Add new team')
@allure.severity('critical')
@pytest.mark.regression
@pytest.mark.parametrize('name', [data.valid_name_of_team_1, data.valid_name_of_team_2])
def test_add_new_team_positive_boundary_value(browser, login, name):
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_manage_team()
    quantity_of_teams_before_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    page.go_to_new_team()
    with allure.step('Enter the name of team'):
        team_name_field = browser.find_element(*PlanningPageLocators.TEAM_NAME_FIELD)
        team_name_field.send_keys(name)
        page.go_to_create_team_btn()
    quantity_of_teams_after_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name="result" + e, attachment_type=AttachmentType.PNG)
    assert quantity_of_teams_after_creation == quantity_of_teams_before_creation + 1


@allure.feature('Add new team')
@allure.severity('critical')
@pytest.mark.regression
def test_add_new_team_but_cancel(browser, login):
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_manage_team()
    quantity_of_teams_before_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    page.go_to_new_team()
    with allure.step('Enter the name of team'):
        page.go_to_team_name_field()
        page.go_to_cancel_team_btn()
    quantity_of_teams_after_creation = len(browser.find_elements(*PlanningPageLocators.ROW_OF_TEAM))
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name="result" + e, attachment_type=AttachmentType.PNG)
    assert quantity_of_teams_after_creation == quantity_of_teams_before_creation


@allure.feature('Add new team')
@allure.severity('critical')
@pytest.mark.regression
@pytest.mark.parametrize('name', [data.invalid_name_of_team_1, data.invalid_name_of_team_2,
                                  data.invalid_name_of_team_3, data.invalid_name_of_team_4])
def test_add_new_team_negative_invalid_name_of_team(browser, login, name):
    page = PlanningPage(browser, urls.LINK_PLANNING)
    page.open()
    page.go_to_manage_team()
    page.go_to_new_team()
    with allure.step('Enter the name of team'):
        team_name_field = browser.find_element(*PlanningPageLocators.TEAM_NAME_FIELD)
        team_name_field.send_keys(name)
        page.go_to_create_team_btn()
    with allure.step('Verify the error message is displayed'):
        error_message_name = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(PlanningPageLocators.ERROR_MESSAGE_NAME)
        )
    text_of_error_message = error_message_name.text
    with allure.step('Make screenshot'):
        e = str(uuid.uuid4().clock_seq)
        allure.attach(browser.get_screenshot_as_png(), name="result" + e, attachment_type=AttachmentType.PNG)
    assert text_of_error_message == "Team name must be 3 to 30 characters long."
