from django.urls import path, re_path, include
from .views import chat_room, chat_detail

urlpatterns=[
   path('api/chat/', chat_room, name='room'),
   path('api/chat/<str:roomName>/<str:userName>', chat_detail, name='chatdetail')
]