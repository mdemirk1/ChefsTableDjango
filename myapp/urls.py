from django.urls import path
from . import models

from myapp import views

urlpatterns = [
    # add url configurations to display specific view when desired url is called index/
    path('index/', views.index),
    path("dishes/<dish>", views.menuItems),
]
