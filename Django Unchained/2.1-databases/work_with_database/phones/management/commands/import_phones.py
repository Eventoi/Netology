import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--create',
            action='store_true',
            default=False,
            help='Импортирование данных'
        )
        
    def handle(self, *args, **options):
        # Phone.objects.filter(all).delete()

        if options['create'] or options['c']:
            with open('phones.csv', 'r') as file:
                phones = list(csv.DictReader(file, delimiter=';'))

            for phone in phones:
                # TODO: Добавьте сохранение модели
                Phone.objects.create(
                    name=phone.get('name'), 
                    image=phone.get('image'), 
                    price=phone.get('price'),
                    release_date=phone.get('release_date'),
                    lte_exists=phone.get('lte_exists'),
                    slug=slugify(phone.get('name')),
                )

        else:
            print('Для импортирования данных введите python manage.py import_phones -c')