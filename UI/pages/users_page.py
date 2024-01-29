from UI.pages.base_page import BasePage
from UI.locators.users_page_locators import UsersPageLocators


class UsersPage(BasePage):

    def go_to_sort_role(self):
        sort_role = self.browser.find_element(*UsersPageLocators.SORT_ROLE)
        sort_role.click()

    def go_to_checkbox_first_user_active(self):
        checkbox_first_user = self.browser.find_element(*UsersPageLocators.CHECKBOX_FIRST_USER)
        checkbox_first_user.click()

    def go_to_deactivate_user(self):
        deactivate_user = self.browser.find_element(*UsersPageLocators.DEACTIVATE_USER)
        deactivate_user.click()

    def go_to_confirm_deactivate(self):
        confirm_deactivate = self.browser.find_element(*UsersPageLocators.CHECKBOX_FIRST_USER)
        confirm_deactivate.click()

    def go_to_select_active_deactivated_user(self):
        select_active_deactivated_user = self.browser.find_element(*UsersPageLocators.SELECT_ACTIVE_DEACTIVATED_USER)
        select_active_deactivated_user.click()

    def go_to_deactivated_user(self):
        deactivated_user = self.browser.find_element(*UsersPageLocators.DEACTIVATED_USER)
        deactivated_user.click()

    def go_to_checkbox_first_user_deactivated(self):
        checkbox_first_user_deactivated = self.browser.find_element(*UsersPageLocators.CHECKBOX_FIRST_USER_DEACTIVATED)
        checkbox_first_user_deactivated.click()

    def go_to_delete_btn(self):
        delete_btn = self.browser.find_element(*UsersPageLocators.DELETE_BTN)
        delete_btn.click()

    def go_to_confirm_delete_btn(self):
        confirm_delete_btn = self.browser.find_element(*UsersPageLocators.CONFIRM_DELETE_BTN)
        confirm_delete_btn.click()


