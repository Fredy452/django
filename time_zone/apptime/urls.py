from django.urls import path

# Importamos views
from . import views

urlpatterns = [
    path('', views.index, name="inicio")
]
