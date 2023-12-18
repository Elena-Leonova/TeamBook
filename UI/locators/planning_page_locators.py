from selenium.webdriver.common.by import By


class PlanningPageLocators:
    USER_MENU = (By.ID, "openUserMenu")
    ADD_USER = (By.CLASS_NAME, "add-user-row__add-button")
    SELECT_USER_FIELD = (By.CSS_SELECTOR, ".tb-react-select-multi__value-container")
    CREATE_NEW_USER = (By.XPATH, "//div[@id='react-select-4-option-0']")
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "email")
    PHONE_NUMBER = (By.ID, "phoneNumber")
    USER_ROLE = (By.CSS_SELECTOR, "#create-user-on-planner > div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 "
                                  "> div > div.MuiDialogContent-root.css-1ty026z > div:nth-child(4) > div > div")
    ROLE_REGULAR = (By.ID, "react-select-15-option-0")
    ROLE_CONTRACTOR = (By.ID, "react-select-15-option-1")
    ROLE_SELF_PLANNER = (By.XPATH, "//div[@id='react-select-5-option-2']")
    ROLE_PLANNER = (By.ID, "react-select-15-option-3")
    ROLE_ADMIN = (By.ID, "react-select-15-option-4")
    TEAMS = (By.CSS_SELECTOR, ".tb-react-select-multi__value-container--has-value")
    REMOVE_CURRENT_TEAM = (By.CSS_SELECTOR, ".css-1txmvc7 > img")
    QA_LEARNING_TEAM_ADD_USER = (By.ID, "react-select-6-option-1")
    GIGO_TEAM_ADD_USER = (By.ID, "react-select-6-option-0")
    SAVE_BTN = (By.CSS_SELECTOR, "#save-created-user p")
    USER_AVATAR = (By.CLASS_NAME, "user-avatar")
    ERROR_MESSAGE_USER_NAME = (By.CLASS_NAME, "form-error__error-text")
    ERROR_MESSAGE_USER_EMAIL = (By.CLASS_NAME, "form-error__error-text")

    GIGO_TEAM = (By.CSS_SELECTOR, "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                  "div.MuiDialogContent-root.css-1ty026z > p > div:nth-child(1) > p")

    QA_LEARNING_TEAM = (By.CSS_SELECTOR, "div.MuiDialog-container.MuiDialog-scrollPaper.css-ekeie0 > div > "
                                         "div.MuiDialogContent-root.css-1ty026z > p > div:nth-child(2) > p")

    TEAM_SELECT = (By.ID, "teamsSelect")
    NEW_TEAM = (By.ID, "newTeam")
    EDIT_TEAM = (By.ID, "editTeam")
    DELETE_TEAM = (By.CSS_SELECTOR, "div.MuiDialogContent-root.css-1ty026z > p > div:nth-child(1) > div > div >"
                                    " img:nth-child(2)")
    TEAM_NAME_FIELD = (By.ID, "teamName")
    CREATE_TEAM_BTN = (By.ID, "createTeamButton")
    CANCEL_TEAM_BTN = (By.CSS_SELECTOR, "div > div.MuiDialogContent-root.css-1ty026z > p > div.manage-team-dialog__"
                                        "team-row.creation > div:nth-child(2) > img:nth-child(2)")
    ROW_OF_TEAM = (By.CLASS_NAME, "manage-team-dialog__team-row")
    ERROR_MESSAGE_NAME = (By.CSS_SELECTOR, "div.MuiDialogContent-root.css-1ty026z > p > div.form-error__error-"
                                           "message.undefined > div > p.form-error__error-text")
    NAME_OF_TEAM = (By.XPATH, "//h2[@id=':ru:']/p/span")
    FIELD_INPUT_TEAM_NAME = (By.XPATH, "//input[@id=':rv:']")
    CONFIRM_DELETE_TEAM = (By.CSS_SELECTOR, "div.MuiDialogActions-root.MuiDialogActions-spacing.css-14b29qc > "
                                            "button:nth-child(1) > p")


