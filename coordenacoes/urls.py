from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('unidade/nova/', views.criar_unidade, name='criar_unidade'),
    path('relacao/nova/', views.criar_relacao, name='criar_relacao'),
]
