__author__ = 'nolram'
from django.core.management.base import NoArgsCommand

from Scripts import teste_tasks_coleta_thread

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        teste_tasks_coleta_thread.testar()
