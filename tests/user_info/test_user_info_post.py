from fixtures.user_info.model import UserInfoRequest


class TestLogin:
    def test_valid_add_user_info(self, app, user):
        """
        Precondition: Register new user
        2. Login user from step 1
        3. Try to add info about user
        4. Check status code is 200
        """
        data, uuid = user
        res_login = app.login.login_user(data=data)
        assert res_login.status_code == 200
        data_user = UserInfoRequest.random()
        token = res_login.data.access_token
        header = {"Authorization": f"JWT {token}"}
        user_info_response = app.user_info.add_user_info(user_id=uuid, data=data_user,
                                                         header=header, type_response=None)
        assert user_info_response.status_code == 200
