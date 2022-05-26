from attrs import validators
from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()

@attr.s
class Address:
    city: str = attr.ib(default=None)
    street: str = attr.ib(default=None)
    home_number: str = attr.ib(default=None)

@attr.s
class UserInfoRequest(BaseClass):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(
            city=fake.city(),
            street=fake.street_name(),
            home_number=fake.building_number(),
        )
        return UserInfoRequest(
            phone=fake.phone_number(), email=fake.email(), address=address
        )


@attr.s
class UserInfoInvalidResponse:
    description: str = attr.ib(validator=validators.instance_of(str))
    error: str = attr.ib(validator=validators.instance_of(str))
    status_code: int = attr.ib(validator=validators.instance_of(int))
