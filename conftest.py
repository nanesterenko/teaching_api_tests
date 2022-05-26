import logging
import pytest
from fixtures.app import App
from fixtures.register.model import RegisterModel, RegisterUserResponse

logger = logging.getLogger("api")

def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    )


@pytest.fixture
def app(request):
    url = request.config.getoption('--api-url')
    logger.info(f"Start api tests, url is {url}")
    return App(url)


@pytest.fixture
def user(app):
    data = RegisterModel.random()
    res = app.register.new_register(data=data, type_response=RegisterUserResponse)
    uuid = res.data.uuid
    assert res.status_code == 201
    return data, uuid



