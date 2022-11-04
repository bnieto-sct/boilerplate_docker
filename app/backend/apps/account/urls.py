"""This file provides the urls for accounts module"""
from django.urls import include, path
from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register(r"user", viewsets.MyUserViewSet, basename="user")

urlpatterns = [path(r"", include(router.urls))]
