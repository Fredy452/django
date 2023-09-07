from django.urls import path

from apps.surveys.views import index, new

urlpatterns = [
    path('', index, name='index'),
    path('new/', new, name='new'),
]