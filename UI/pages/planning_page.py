import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data
from UI.locators.planning_page_locators import PlanningPageLocators
from UI.pages.base_page import BasePage
import uuid


class PlanningPage(BasePage):
    def go_to_add_user(self):
        add_user = self.browser.find_element(*PlanningPageLocators.ADD_USER)
        add_user.click()

    def go_to_select_user_field(self):
        select_user_field = self.browser.find_element(*PlanningPageLocators.SELECT_USER_FIELD)
        select_user_field.click()

    def go_to_create_new_user(self):
        create_new_user = self.browser.find_element(*PlanningPageLocators.CREATE_NEW_USER)
        create_new_user.click()

    def go_to_user_first_name(self):
        word = str(uuid.uuid4().hex[:2])
        user_first_name = self.browser.find_element(*PlanningPageLocators.FIRST_NAME)
        user_first_name.send_keys(data.PlanningData.valid_first_name_of_user + word)

    def go_to_user_last_name(self):
        word = str(uuid.uuid4().hex[:2])
        user_last_name = self.browser.find_element(*PlanningPageLocators.LAST_NAME)
        user_last_name.send_keys(data.PlanningData.valid_last_name_of_user + word)

    def go_to_user_email(self):
        user_email = self.browser.find_element(*PlanningPageLocators.EMAIL)
        e = str(uuid.uuid4().clock_seq)
        user_email.send_keys(e + data.PlanningData.valid_email_user)

    def go_to_user_phone_number(self):
        user_phone_number = self.browser.find_element(*PlanningPageLocators.PHONE_NUMBER)
        user_phone_number.send_keys(data.PlanningData.valid_user_phone_number)

    def go_to_user_role(self):
        user_role = self.browser.find_element(*PlanningPageLocators.USER_ROLE)
        user_role.click()
        self.browser.find_element(*PlanningPageLocators.ROLE_SELF_PLANNER).click()

    def go_to_user_choose_qa_learning_team(self):
        user_team = self.browser.find_element(*PlanningPageLocators.TEAMS)
        user_team.click()
        remove_current_team = self.browser.find_element(*PlanningPageLocators.REMOVE_CURRENT_TEAM)
        remove_current_team.click()
        self.browser.find_element(*PlanningPageLocators.QA_LEARNING_TEAM_ADD_USER).click()

    def go_to_user__choose_gigo_team(self):
        user_team = self.browser.find_element(*PlanningPageLocators.TEAMS)
        user_team.click()
        remove_current_team = self.browser.find_element(*PlanningPageLocators.REMOVE_CURRENT_TEAM)
        remove_current_team.click()
        self.browser.find_element(*PlanningPageLocators.GIGO_TEAM_ADD_USER).click()

    def go_to_manage_team(self):
        team_select = self.browser.find_element(*PlanningPageLocators.TEAM_SELECT)
        team_select.click()

    def go_to_gigo_team(self):
        team_select = self.browser.find_element(*PlanningPageLocators.TEAM_SELECT)
        team_select.click()
        gigo_team = self.browser.find_element(*PlanningPageLocators.GIGO_TEAM)
        gigo_team.click()

    def go_to_qa_learning_team(self):
        team_select = self.browser.find_element(*PlanningPageLocators.TEAM_SELECT)
        team_select.click()
        qa_learning_team = self.browser.find_element(*PlanningPageLocators.QA_LEARNING_TEAM)
        qa_learning_team.click()

    def go_to_user_save_btn(self):
        save_btn = self.browser.find_element(*PlanningPageLocators.SAVE_BTN)
        save_btn.click()

    def go_to_new_team(self):
        new_team = self.browser.find_element(*PlanningPageLocators.NEW_TEAM)
        new_team.click()

    def go_to_team_name_field(self):
        team_name_field = self.browser.find_element(*PlanningPageLocators.TEAM_NAME_FIELD)
        e = str(uuid.uuid4().clock_seq)
        team_name_field.send_keys(data.PlanningData.valid_name_of_team + e)

    def go_to_create_team_btn(self):
        create_team_btn = self.browser.find_element(*PlanningPageLocators.CREATE_TEAM_BTN)
        create_team_btn.click()

    def go_to_cancel_team_btn(self):
        cancel_team_btn = self.browser.find_element(*PlanningPageLocators.CANCEL_TEAM_BTN)
        cancel_team_btn.click()

    def go_to_delete_team_btn(self):
        delete_team_btn = self.browser.find_element(*PlanningPageLocators.DELETE_TEAM)
        delete_team_btn.click()

    def go_to_field_input_team_name(self):
        name_of_team = self.browser.find_element(*PlanningPageLocators.NAME_OF_TEAM)
        text_of_name_of_team = name_of_team.text
        field_input_team_name = self.browser.find_element(*PlanningPageLocators.FIELD_INPUT_TEAM_NAME)
        field_input_team_name.send_keys(text_of_name_of_team)

    def go_to_confirm_delete_team(self):
        confirm_delete_team = self.browser.find_element(*PlanningPageLocators.CONFIRM_DELETE_TEAM)
        confirm_delete_team.click()


