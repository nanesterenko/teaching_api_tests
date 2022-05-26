from attrs import validators
from faker import Faker
import attr

fake = Faker()


@attr.s
class LoginUserResponse:
    access_token: str = attr.ib(validator=validators.instance_of(str))

@attr.s
class LoginUserInvalidResponse:
    description: str = attr.ib(validator=validators.instance_of(str))
    error: str = attr.ib(validator=validators.instance_of(str))
    status_code: int = attr.ib(validator=validators.instance_of(int))
