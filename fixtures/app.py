from fixtures.auth.api import Login
from fixtures.register.api import Register
from fixtures.requests import Client
from fixtures.user_info.api import UserInfo


class App:
    def __init__(self, url: str):
        self.client = Client
        self.url = url
        self.register = Register(self)
        self.login = Login(self)
        self.user_info = UserInfo(self)
        