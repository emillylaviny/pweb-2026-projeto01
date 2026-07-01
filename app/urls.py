from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sobre/', views.sobre, name="sobre"),
    path('elenco/', views.elenco, name="elenco"),
    path('', views.inicio, name="inicio"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)