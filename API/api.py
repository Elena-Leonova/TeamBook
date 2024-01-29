import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()


class TeamBook:
    """ API library to the website https://web.teambooktest.com/ """

    def __init__(self):
        self.base_url = "https://web.teambooktest.com/api"

    def get_token(self) -> json:
        """ Request to Swagger to get login token (valid email and password) """
        data = {
            "user[email]": os.environ['LOGIN'],
            "user[password]": os.environ['PASSWORD']
        }
        res = requests.post(self.base_url + "/auth/login", data=data)
        text = res.text
        formatted_text = text.replace('"', "").replace('{', "").replace('}', "").replace(":", "").replace("=>", ': ')
        data = {i.split(': ')[0]: i.split(': ')[1] for i in formatted_text.split(', ')}
        my_token = data['token']
        status = res.status_code
        return my_token, status

    def login_email(self) -> json:
        """ Request to Swagger to log in user(valid and invalid email + valid password) """
        data = {
            "user[email]": os.environ['LOGIN'],
            "user[password]": os.environ['PASSWORD']
        }
        res = requests.post(self.base_url + "/auth/login", data=data)
        status = res.status_code
        return status

    def forgot_password(self) -> json:
        """ Request to Swagger to get code to update password """
        data = {
            "email": os.environ['LOGIN']
        }
        res = requests.post(self.base_url + "/auth/forgot_password", data=data)
        status = res.status_code
        return status

    def update_password(self) -> json:
        """ Request to Swagger to update password """
        data = {
            "code": "922c9cb4",
            "password": "Mynameislena1!"
        }
        res = requests.post(self.base_url + "/auth/update_password", data=data)
        status = res.status_code
        return status


