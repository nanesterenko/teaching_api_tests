from common.deco import log
from fixtures.auth.model import LoginUserResponse
from fixtures.user_info.model import UserInfoRequest
from fixtures.validator import Validator


class UserInfo(Validator):
    def __init__(self, app):
        self.app = app

    POST_USER_INFO = '/user_info/{}'

    @log('Login user')
    def add_user_info(self, user_id: int, data: UserInfoRequest, header=None, type_response=LoginUserResponse):
        res = self.app.client.request('POST', f"{self.app.url}{self.POST_USER_INFO.format(user_id)}",
                         json=data.to_dict(), headers=header)
        return self.structure(res, type_response)
