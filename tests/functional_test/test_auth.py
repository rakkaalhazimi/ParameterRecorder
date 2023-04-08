import pytest
from flask.testing import FlaskClient
from flask import Response

from app.auth import services


class AuthActions:
    def __init__(self, client: FlaskClient):
        self.client = client

    def login(self, email: str, password: str) -> Response:
        data = {
            "email": email,
            "password": password,
        }
        return self.client.post("/auth/login", data=data)

    def register(self, email: str, password: str, confirm_password: str) -> Response:
        data = {
            "email": email,
            "password": password,
            "confirm_password": confirm_password
        }
        return self.client.post("auth/register", data=data)

    def logout(self) -> Response:
        return self.client.get("auth/logout", follow_redirects=True)


@pytest.fixture
def auth(client):
    return AuthActions(client)


def test_redirect_login(client: FlaskClient):
    """
    GIVEN user haven't logged in
    WHEN user access home page
    THEN redirect user to login page
    """
    response = client.get("/", follow_redirects=True)
    assert "/login" in response.request.path


def test_redirect_login_after_logout(auth: AuthActions):
    """
    GIVEN user have logged in
    WHEN user press logout button
    THEN redirect user to login page
    """
    response = auth.logout()
    assert "/login" in response.request.path


def test_register_user(auth: AuthActions):
    """
    GIVEN user doesn't have account or about to create new account
    WHEN user register new account successfully
    THEN user have new account
    """
    email = "test"
    password = "test"
    auth.register(email=email, password=password, confirm_password=password)
    user = services.find_user(email=email)
    assert user is not None


def test_hash_user_password(auth: AuthActions):
    """
    GIVEN user is registering new account
    WHEN user finished the registration form
    THEN user password must be stored in hashed format
    """
    email = "test"
    password = "test"
    auth.register(email=email, password=password, confirm_password=password)
    user = services.find_user(email=email)
    assert services.check_user_password(user.password, password)