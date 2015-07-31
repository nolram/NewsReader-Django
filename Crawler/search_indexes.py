__author__ = 'nolram'

import datetime
from haystack import indexes
from Crawler.models import Postagens


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    texto = indexes.CharField(model_attr='texto')
    horario_postagem_site = indexes.DateTimeField(model_attr='horario_postagem_site')

    def get_model(self):
        return Postagens

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(horario_postagem_site__lte=datetime.datetime.now())
