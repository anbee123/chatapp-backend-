from django.urls import path, re_path, include
from . import views

urlpatterns=[
   # path('', views.index, name='index'),
   re_path(r'^$', views.chat_list),
   re_path(r'^(?P<pk>[0-9]+)$', views.chat_detail)
]