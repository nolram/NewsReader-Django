__author__ = 'nolram'
from django.core.management.base import NoArgsCommand

from Crawler.add_some_sites import PrimeiraAdicao

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        pa = PrimeiraAdicao()
        pa.add_pages()
