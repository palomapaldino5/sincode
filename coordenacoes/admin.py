from django.contrib import admin
from .models import UnidadeCoordenada, ConectorCoordenativo, TipoRelacao, RelacaoCoordenativa

admin.site.register(UnidadeCoordenada)
admin.site.register(TipoRelacao)
admin.site.register(ConectorCoordenativo)
admin.site.register(RelacaoCoordenativa)
