from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from Crawler.utils import run_crawler

logger = get_task_logger(__name__)

__author__ = 'nolram'


@periodic_task(
    run_every=(crontab(minute='*/5')),
    name="crawling_news_rss",
    ignore_result=True
)
def do_crawling():
    run_crawler()
    logger.info("Crawling News Concluido")
