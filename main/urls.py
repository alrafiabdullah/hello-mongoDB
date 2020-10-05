from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('api/v1/users', views.UserList.as_view()),
    path('api/v1/users/new', views.UserCreate.as_view()),
]
