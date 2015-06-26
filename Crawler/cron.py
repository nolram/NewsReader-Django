# -.- encoding: utf-8 -.-
__author__ = 'marlon'

import feedparser as fp
from .models import Categorias, LinksRSS, Postagens, Sites, Tags, TagsPostagens


#class CronColeta(CronJobBase):
#    RUN_EVERY_MINS = 60

#    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#    code = 'Crawler.cron'    # a unique code

def do_crawler(self):
    sites = LinksRSS.objects.all()
    for site in sites:
        coleta = fp.parse(site.link_rss)
        for col in coleta["items"]:
            post = Postagens.objects.get_or_create(link=col["wfw_commentrss"].replace("feed/", ""),
                                                   defaults={"titulo": col["title"],
                                                             "texto": col["summary"]})
            post.save()
            for tag in col["tags"]:
                db_tag = Tags(tag=tag["term"].lower())
                db_tag.save()
                tpos = TagsPostagens(fk_tag=db_tag, fk_postagem=post)
                tpos.save()

        print("Salvo reportagem")