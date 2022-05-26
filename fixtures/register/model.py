from attrs import validators
from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class RegisterModel(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        username = fake.email()
        password = fake.password()
        return RegisterModel(username=username, password=password)


@attr.s
class RegisterUserResponse:
    message: str = attr.ib(validator=validators.instance_of(str))
    uuid: int = attr.ib(validator=validators.instance_of(int))

@attr.s
class RegisterUserInvalidResponse:
    message: str = attr.ib(validator=validators.instance_of(str))