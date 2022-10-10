import uuid
import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register
from tests.partners.factories import PartnerFactory


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def test_password():
    return 'fx.s2d'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return make_user


@pytest.fixture
def auto_login_user(db, client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user
    return make_auto_login


# To register a factory you need `pytest-factoryboy` installed
register(PartnerFactory)
