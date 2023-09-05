from django.urls import path
from . import views


urlpatterns = [
    path('', views.random_word, name="word"),
    path('word', views.word, name="get_word"),
    path('reset', views.reset, name="borrar"),
]