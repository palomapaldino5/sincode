from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nova-unidade/', views.criar_unidade, name='criar_unidade'),
    path('novo-tipo-relacao/', views.criar_tipo_relacao, name='criar_tipo_relacao'),
]
