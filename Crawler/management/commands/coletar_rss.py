__author__ = 'nolram'
import kronos

from django.core.management.base import NoArgsCommand

from scripts import crawler_rss_thread_v2

@kronos.register('*/15 * * * *')
class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        crawler_rss_thread_v2.run()
