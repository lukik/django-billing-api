import json
import pytest
import pprint

from model_bakery import baker
from factory.faker import faker

from partners.models import Partner

pp = pprint.PrettyPrinter(indent=4, width=80)


fake = faker.Faker()

# Mark to access DB
pytestmark = pytest.mark.django_db


class TestPartnerEndpoints:

    endpoint = '/v1/partners/'

    def test_list(self, api_client, auto_login_user):
        """
        Retrieve list of entries from the DB
        Note: Used model-bakery.baker to generate data which easily creates fixtures (but very random data)
        """
        baker.make(Partner, _quantity=3)

        api_client, user = auto_login_user()

        response = api_client.get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)['results']) == 3

    def test_create(self, api_client, auto_login_user):
        """
        Create a DB entry
        Note: Used Factory Boy to Generate data
        """
        # Login the user
        api_client, user = auto_login_user()

        payload = {
            'title': fake.name(),
            'notes': fake.sentence(),
            'is_client': True,
            'is_supplier': False,
            'status': 1
        }
        response = api_client.post(
            self.endpoint,
            data=payload,
            format='json'
        )
        assert response.status_code == 201

    def test_retrieve(self, api_client, auto_login_user, partner_factory):
        """
        Retrieve a record from the DB.
        Note: Used DjangoModelFactory to create the entry with the fixture found under `partners.factories`
        """
        # Login the user
        api_client, user = auto_login_user()

        # Create DB entry using DjangoModelFactor fixture
        partner = partner_factory.create(created_by=user)

        url = f'{self.endpoint}{partner.id}/'

        response = api_client.get(url)

        assert response.status_code == 200

    def test_update(self, rf, api_client, auto_login_user):
        """
        Update a DB Entry
        """
        # Login the user
        api_client, user = auto_login_user()

        is_client = True

        old_partner = baker.make(Partner)
        new_partner = baker.prepare(Partner)
        update_dict = {
            'title': new_partner.title,
            'notes': new_partner.notes,
            'is_client': is_client,
            'status': 1
        }

        url = f'{self.endpoint}{old_partner.id}/'

        response = api_client.patch(
            url,
            update_dict,
            content_type='application/json',
        )

        assert response.status_code == 200
        assert json.loads(response.content)['title'] == new_partner.title
        assert json.loads(response.content)['is_client'] == is_client

    def test_delete(self, api_client, auto_login_user):
        """
        Delete a DB Entry
        """
        api_client, user = auto_login_user()

        partner = baker.make(Partner)

        url = f'{self.endpoint}{partner.id}/'

        payload = {
            'delete_reason': 'Testing Deletion'
        }

        response = api_client.delete(
            url,
            data=payload,
            content_type='application/json',
        )

        assert response.status_code == 204
