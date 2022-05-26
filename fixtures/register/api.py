from common.deco import log
from fixtures.register.model import RegisterModel
from fixtures.validator import Validator


class Register(Validator):
    def __init__(self, app):
        self.app = app

    POST_REGISTER = '/register'

    @log('Register new user')
    def new_register(self, data: RegisterModel, type_response=None):
        res = self.app.client.request('POST', f"{self.app.url}{self.POST_REGISTER}",
                            json=data.to_dict())
        return self.structure(res, type_response)