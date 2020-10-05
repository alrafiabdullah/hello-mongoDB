from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError
from django.conf import settings
from django.contrib import auth

from .models import User
from .serializers import UserSerializer
# Create your views here.


def index(request):
    return render(request, "main/index.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["usernamee"]
        password = request.POST["passwordd"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "main/index.html", {
                "message": "Incorrect username/password"
            })
    return render(request, "main/index.html")


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))


class UserPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 100


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('id', )
    search_fields = ('username', )
    pagination_class = UserPagination


class UserCreate(CreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = User.objects.all()
        return user

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.create()
            data["response"] = "Successfully registered!"
        else:
            data = serializer.errors
        return Response(data)
