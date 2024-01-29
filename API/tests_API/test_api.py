import os

import pytest
import requests

import data
from API.api import TeamBook

tb = TeamBook()


def test_get_token():
    token = tb.get_token()[0]
    status = tb.get_token()[1]
    assert token
    assert status == 201


@pytest.mark.parametrize('email, expected_result',
                         [(os.environ['LOGIN'], 201),
                          (data.RegistrationLoginData.invalid_email_1, 403),
                          (data.RegistrationLoginData.invalid_email_2, 403),
                          (data.RegistrationLoginData.not_existed_email, 403),
                          ])
def test_login_email(email, expected_result):
    d = {
        "user[email]": email,
        "user[password]": os.environ['PASSWORD']
    }
    res = requests.post(tb.base_url + "/auth/login", data=d)
    status = res.status_code
    assert status == expected_result


@pytest.mark.parametrize('password, expected_result',
                         [(os.environ['PASSWORD'], 201),
                          (data.RegistrationLoginData.incorrect_password_1, 403),
                          (data.RegistrationLoginData.incorrect_password_2, 403),
                          (data.RegistrationLoginData.password_without_numbers, 403),
                          (data.RegistrationLoginData.password_without_letters, 403),
                          (data.RegistrationLoginData.password_less_8_symbols, 403),
                          ])
def test_login_password(password, expected_result):
    d = {
        "user[email]": os.environ['LOGIN'],
        "user[password]": password
    }
    res = requests.post(tb.base_url + "/auth/login", data=d)
    status = res.status_code
    assert status == expected_result


# @pytest.mark.parametrize('email, expected_result',
#                          [(os.environ['LOGIN'], 201),
#                           (data.RegistrationLoginData.invalid_email_1, 403),
#                           ])
# def test_forgot_password(email, expected_result):
#     d = {
#         'email': email
#     }
#     res = requests.post(tb.base_url + "/auth/forgot_password", data=d)
#     status = res.status_code
#     assert status == expected_result

# @pytest.mark.parametrize('code, expected_result',
#                          [('0b4d5168', 201),
#                           ('dfg852', 422),
#                           ])
# def test_update_password(code, expected_result):
#     d = {
#         'code': code,
#         'password': os.environ['PASSWORD']
#     }
#     res = requests.post(tb.base_url + '/auth/update_password', data=d)
#     status = res.status_code
#     assert status == expected_result


# @pytest.mark.parametrize('password, expected_result',
#                          [(os.environ['PASSWORD'], 201),
#                           (data.RegistrationLoginData.password_less_8_symbols, 422),
#                           ])
# def test_update_password(password, expected_result):
#     d = {
#         'code': '6250a11e',
#         'password': os.environ['PASSWORD']
#     }
#     res = requests.post(tb.base_url + '/auth/update_password', data=d)
#     status = res.status_code
#     assert status == expected_result
