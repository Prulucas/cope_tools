from django.urls import path
from . import views

urlpatterns = [
    # Rota do ecrã do formulário
    path('', views.index, name='index'),

    # Rota da API REST
    path('api/upper/', views.api_send_to_upper, name='api_upper'),
]
