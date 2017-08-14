from django.core.management.base import BaseCommand
from Crawler.add_some_sites import PrimeiraAdicao

__author__ = 'nolram'


class Command(BaseCommand):
    def handle(self, *args, **options):
        pa = PrimeiraAdicao()
        pa.add_pages()
