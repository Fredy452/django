from django import views
from django.urls import path

from apps.blogs.views import index, new, create, show, edit, delete

urlpatterns = [
    path('', index, name='index'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('<int:number>/', show, name='show'),
    path('<int:number>/edit', edit, name='edit'),
    path('<int:number>/delete', delete, name='delete'),
]