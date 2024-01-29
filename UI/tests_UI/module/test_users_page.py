import time
import uuid

from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC

import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait

from UI.pages.users_page import UsersPage
import urls
from UI.locators.users_page_locators import UsersPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@allure.feature('Delete user')
@allure.severity('major')
@pytest.mark.regression
def test_deactivate_user(browser, login):
    page = UsersPage(browser, urls.LINK_USERS)
    page.open()
    time.sleep(3)
    page.go_to_sort_role()
    row_of_user_before_deactivation = len(browser.find_elements(*UsersPageLocators.ROW_OF_USER_ACTIVE))
    page.go_to_checkbox_first_user_active()
    page.go_to_deactivate_user()
    time.sleep(3)
    element = browser.find_element(By.XPATH, "//button[.='Deactivate']")
    ActionChains(browser).move_to_element(element).click().perform()
    time.sleep(3)
    row_of_user_after_deactivation = len(browser.find_elements(*UsersPageLocators.ROW_OF_USER_ACTIVE))
    with allure.step('Make screenshot'):
        num = str(uuid.uuid4().clock_seq)
    allure.attach(browser.get_screenshot_as_png(), name='result' + num, attachment_type=AttachmentType.PNG)
    assert row_of_user_before_deactivation != row_of_user_after_deactivation


@allure.feature('Delete user')
@allure.severity('major')
@pytest.mark.regression
def test_delete_user(browser, login):
    page = UsersPage(browser, urls.LINK_USERS)
    page.open()
    page.go_to_select_active_deactivated_user()
    page.go_to_deactivated_user()
    time.sleep(2)
    page.go_to_checkbox_first_user_deactivated()
    with allure.step("Verify delete_btn is displayed"):
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(UsersPageLocators.DELETE_BTN)
                )
    page.go_to_delete_btn()
    page.go_to_confirm_delete_btn()
    no_records = browser.find_element(*UsersPageLocators.NO_RECORDS)
    with allure.step('Make screenshot'):
        num = str(uuid.uuid4().clock_seq)
    allure.attach(browser.get_screenshot_as_png(), name='result' + num, attachment_type=AttachmentType.PNG)
    assert no_records.is_displayed()
