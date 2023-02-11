from django.core.management.base import BaseCommand
from faker import Faker
from random import uniform
from api.models import Item


class Command(BaseCommand):
    halp = 'Create fake data'

    def handle(self, *args, **options):
        faker = Faker()
        for _ in range(5):
            Item.objects.create(name=faker.word(),
                                description=faker.text(),
                                price=round(uniform(1, 100), 1))
