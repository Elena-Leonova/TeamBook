import uuid

from .base_page import BasePage
from UI.locators.registration_page_locators import RegistrationPageLocators
import os
from dotenv import load_dotenv

load_dotenv()


class RegistrationPage(BasePage):
    def go_to_reg_first_name(self):
        first_name = self.browser.find_element(*RegistrationPageLocators.REG_FIRST_NAME)
        first_name.clear()
        first_name.send_keys("Abc")

    def go_to_reg_last_name(self):
        last_name = self.browser.find_element(*RegistrationPageLocators.REG_LAST_NAME)
        last_name.clear()
        last_name.send_keys("Xyz")

    def go_to_reg_business_email(self):
        business_email = self.browser.find_element(*RegistrationPageLocators.REG_BUSINESS_EMAIL)
        business_email.clear()
        e = str(uuid.uuid4().clock_seq)
        business_email.send_keys(os.environ[e + 'VALID_REG_BUSINESS_EMAIL'])

    def go_to_reg_organization(self):
        organization = self.browser.find_element(*RegistrationPageLocators.REG_ORGANIZATION)
        organization.clear()
        organization.send_keys("QALearning")

    def go_to_reg_password(self):
        reg_password = self.browser.find_element(*RegistrationPageLocators.REG_PASSWORD)
        reg_password.clear()
        reg_password.send_keys(os.environ['REG_PASSWORD'])

    def go_to_reg_checkbox(self):
        checkbox = self.browser.find_element(*RegistrationPageLocators.REG_CHECKBOX)
        checkbox.click()

    def go_to_reg_create_org_btn(self):
        create_org_btn = self.browser.find_element(*RegistrationPageLocators.REG_CREATE_ORG_BTN)
        create_org_btn.click()

    def go_to_reg_skip_btn(self):
        skip_btn = self.browser.find_element(*RegistrationPageLocators.REG_SKIP)
        skip_btn.click()



