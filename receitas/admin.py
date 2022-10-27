from django.contrib import admin
from .models import Receita

class ListandoReceita(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'modo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    list_editable = ('publicada',)
    search_fields = ('nome_receita',)
    list_filter = ('pessoa',)

admin.site.register(Receita, ListandoReceita)
