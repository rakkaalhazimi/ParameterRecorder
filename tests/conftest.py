import pytest

from app import create_app, clear_database
from app.config import TestConfig


@pytest.fixture
def test_app():
    app = create_app(TestConfig)
    yield app
    clear_database()

@pytest.fixture
def client(test_app):
    return test_app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()