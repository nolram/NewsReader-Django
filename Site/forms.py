__author__ = 'nolram'

from django import forms

class PesquisaForms(forms.Form):
    query = forms.CharField(label="Pesquisa", max_length=120)
    page = forms.IntegerField(min_value=1, required=False)
