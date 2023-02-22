from django.urls import path, re_path, include
from .views import chat_room, chat_detail, chat_edit

urlpatterns=[
   path('api/chat/', chat_room, name='room'),
   path('api/chat/<str:roomName>', chat_detail, name='chatdetail'),
   path('api/chat/edit/<int:pk>', chat_edit, name='chatedit')
]