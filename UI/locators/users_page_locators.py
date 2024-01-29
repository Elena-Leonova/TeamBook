from selenium.webdriver.common.by import By


class UsersPageLocators:
    SORT_ROLE = (By.XPATH, "//div[.='Role']")
    CHECKBOX_FIRST_USER = (By.CSS_SELECTOR, "div.users-page__users-content > div.users-page__user-list > "
                                            "div:nth-child(1) > div > div.user-block__select-checkbox > img")
    DEACTIVATE_USER = (By.ID, "deactivateUserPageButton")
    ROW_OF_USER_ACTIVE = (By.CLASS_NAME, "user-list__block")
    CONFIRM_DEACTIVATE = (By.XPATH, "//button[.='Deactivate']")

    SELECT_ACTIVE_DEACTIVATED_USER = (By.CLASS_NAME, "deactivate-dropdown__container")
    DEACTIVATED_USER = (By.XPATH, "//div[.='Deactivated']")
    ACTIVE_USER = (By.ID, "react-select-4-option-0")
    CHECKBOX_FIRST_USER_DEACTIVATED = (By.CLASS_NAME, "user-block__select-checkbox")
    DELETE_BTN = (By.ID, "deleteUserPageButton")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[.='Delete']")
    ROW_OF_USER = (By.CLASS_NAME, "users-page__user-list")
    NO_RECORDS = (By.CSS_SELECTOR, "div.users-page__users-content > div.users-page__user-list > p > b")

