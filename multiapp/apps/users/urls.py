from django.urls import path, include


from apps.users.views import register, login, index
from apps.blogs.views import index as blog_index

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('users/new/', register, name='new'),
    path('users/', index, name='index'),
    path('', blog_index, name="blog_index"),
]