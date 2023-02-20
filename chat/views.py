<<<<<<< HEAD
from django.http import JsonResponse
from chat.models import Room

def index(request):
    rooms = Room.objects.all()
    data = list(rooms.values())
    return JsonResponse(data, safe=False)
=======
from django.shortcuts import render
from django.http import HttpResponse
from .models import Message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# from .serializers import MessageSerializer

def index(request):
  return HttpResponse('<h1> MY INDEX PAGE </h1>')

class Message(APIView):

  def get(self, request):
    # Index Request
    print(request)
    # Get all messages from the chat table
    messages = Message.objects.all()
    # Use serializer to format table data to JSON
    data = MessageSerializer(messages, many=True).data
    return Response(data)
  
  def post(self, request):
    # Post Request
    print(request.data)
    # format data for postgres
    chat = MessageSerializer(data=request.data)
    if chat.is_valid():
      chat.save()
      return Response(chat.data, status=status.HTTP_201_CREATED)
    else: 
      return Response(chat.errors, status=status.HTTP_400_BAD_REQUEST)
    
>>>>>>> bf4c2610c2a987e0258c112c9c133d774a8dde18
