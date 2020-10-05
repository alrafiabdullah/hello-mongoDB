from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('register', views.registration_view, name='register')
    path('api/v1/users', views.UserList.as_view()),
    path("api/v1/users/new", views.UserCreate.as_view()),

]
