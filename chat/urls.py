from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # <- empty string means Root, do not add a "/"
]
