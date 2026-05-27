from django.urls import path
from app import views

urlpatterns = [
    path('sobre/', views.sobre, name="sobre"),
    path('elenco/', views.elenco, name="elenco"),
    path('', views.inicio, name="inicio"),
]