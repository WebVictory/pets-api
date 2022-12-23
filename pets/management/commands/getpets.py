import argparse
import json
from django.core.management.base import BaseCommand
from django.http import HttpRequest

from pets.views import PetsViewSet
from pets_api.settings import API_KEY, DEFAULT_DOMAIN, DEFAULT_PORT


class Command(BaseCommand):
    help = 'Выгрузка питомцев из командной строки'

    def handle(self, *args, **options):
        django_request = HttpRequest()
        has_photos = options.get("has_photos")
        django_request.method = 'GET'
        if has_photos is True:
            django_request.GET['has_photos'] = 'true'
        elif has_photos is False:
            django_request.GET['has_photos'] = 'false'

        django_request.META['SERVER_NAME'] = DEFAULT_DOMAIN
        django_request.META['SERVER_PORT'] = DEFAULT_PORT
        django_request.META['HTTP_X-API-KEY'] = API_KEY
        my_view = PetsViewSet.as_view({'get': 'list'})
        data = my_view(request=django_request)
        items = data.data["items"]
        self.stdout.write(json.dumps({"pets": items}))

    def add_arguments(self, parser):
        parser.add_argument('--has-photos', action=argparse.BooleanOptionalAction)