__author__ = 'nolram'
from django.core.management.base import NoArgsCommand

from idlelib.PyShell import main

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        main()
