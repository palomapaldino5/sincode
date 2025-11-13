from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('noticias.urls')),
    path('', include('associados.urls')),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coordenacoes.urls')),  # 🆕 adiciona o app coordenacoes
]
