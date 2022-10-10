import factory
import uuid
from faker import Faker

from partners.models import Partner


faker = Faker()


class PartnerFactory(factory.django.DjangoModelFactory):
    """
    This class defines the Factory Class for Partner Model.

    Its data is populated using Faker which requires `factory-boy` to be installed
    """

    class Meta:
        model = Partner

    created_by = uuid.uuid4()
    title = faker.word()
    account_number = faker.random_int(min=1, max=99999)
    status = faker.random_int(min=1, max=4)
    notes = faker.sentence()[:200]
    is_client = faker.boolean()
    is_supplier = faker.boolean()
