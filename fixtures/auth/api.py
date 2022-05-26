from common.deco import log
from fixtures.auth.model import LoginUserResponse
from fixtures.register.model import RegisterModel
from fixtures.validator import Validator


class Login(Validator):
    def __init__(self, app):
        self.app = app

    POST_LOGIN = '/auth'

    @log('Login user')
    def login_user(self, data: RegisterModel, type_response=LoginUserResponse):
        res = self.app.client.request('POST', f"{self.app.url}{self.POST_LOGIN}",
                            json=data.to_dict())
        return self.structure(res, type_response)