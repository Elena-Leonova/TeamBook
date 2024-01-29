class RegistrationLoginData:
    existed_email = "test@gmail.com"
    not_existed_email = '123456@gmail.com'
    invalid_email_1 = 'testgmail.com'
    invalid_email_2 = '@gmail.com'
    password_less_8_symbols = 'A123456'
    password_without_letters = '12345678'
    password_without_numbers = 'sdfghjklcvb'
    incorrect_password_1 = 'a1234567!'
    incorrect_password_2 = 'A1234567'


class PlanningData:
    empty_name_of_team = ""
    blank_name_of_team = " "
    name_of_team_less_3_chars = "qa"
    name_of_team_more_30_chars = "qa123456789876543210alhtdgejdss"
    valid_name_of_team = 'qa_team'
    name_of_team_30_chars = "qa123456789876543210alhtdgejds"
    name_of_team_3_chars = "qaL"

    valid_first_name_of_user = "Pasha"
    first_name_of_user_32_chars = "cyclopentanoperhydrophenanthre"
    first_name_of_user_empty = ""
    blank_first_name_of_user = " "
    first_name_of_user_less_2_chars = "o"
    first_name_of_user_more_32_chars = "cyclopentanoperhydrophenanthrenes"

    valid_last_name_of_user = "Petrov"
    last_name_of_user_32_chars = "cyclopentanoperhydrophenanthre"
    last_name_of_user_empty = ""
    blank_last_name_of_user = " "
    last_name_of_user_less_2_chars = "o"
    last_name_of_user_more_32_chars = "cyclopentanoperhydrophenanthrenes"

    valid_user_phone_number = "0533987231"
    phone_number_less_6_digits = "12345"
    phone_number_more_14_digits = "123456789876543"
    phone_number_letters = "djkshsk"

    valid_email_user = '123@gmail.com'
