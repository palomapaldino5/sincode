from django.contrib import admin
from .models import TipoRelacao, ConectorCoordenativo, UnidadeCoordenada


@admin.register(TipoRelacao)
class TipoRelacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)


@admin.register(ConectorCoordenativo)
class ConectorCoordenativoAdmin(admin.ModelAdmin):
    list_display = ('id', 'termo', 'tipo_relacao')
    list_filter = ('tipo_relacao',)
    search_fields = ('termo',)


@admin.register(UnidadeCoordenada)
class UnidadeCoordenadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'conteudo', 'conector')
    list_filter = ('conector',)
    search_fields = ('conteudo',)
