from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="inicio"),
    path('users', views.create_user)
]