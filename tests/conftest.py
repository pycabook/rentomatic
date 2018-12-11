import pytest


from rentomatic.app import create_app
from rentomatic.flask_settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)


def pytest_addoption(parser):
    parser.addoption("--integration", action="store_true",
                     help="run integration tests")


def pytest_runtest_setup(item):
    if 'integration' in item.keywords and not \
            item.config.getvalue("integration"):
        pytest.skip("need --integration option to run")
