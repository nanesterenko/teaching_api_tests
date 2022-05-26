import pytest

from fixtures.register.model import RegisterModel, RegisterUserResponse
from fixtures.auth.model import LoginUserInvalidResponse


class TestLogin:
    def test_valid_login(self, app, user):
        """
        1. Register new user
        2. Try to auth user from step 1
        3. Check status code is 200
        """
        res_login = app.login.login_user(data=user)
        assert res_login.status_code == 200


    def test_nonexist_user_login(self, app):
        user = RegisterModel.random()
        login_response = app.login.login_user(data=user, type_response=LoginUserInvalidResponse)
        assert login_response.status_code == 401
        assert login_response.data.description == "Invalid credentials"
        assert login_response.data.error == 'Bad Request'

