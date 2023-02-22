from django.shortcuts import render
# from django.http import HttpResponse
from django.http.response import JsonResponse
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from chat.models import Chat
from chat.serializers import ChatSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

def index(request):
  return HttpResponse('<h1> MY INDEX PAGE </h1>')

@api_view(['GET', 'DELETE'])
def chat_detail(request, roomName):
  if request.method == "GET":
    messages = Chat.objects.filter(roomName=roomName)
    serializer = ChatSerializer(messages, many=True)
    return JsonResponse(serializer.data, safe=False)
  # if request.method == "DELETE":
  #   room = Chat.objects.filter(roomName=roomName)
  #   room.delete()
  #   return JsonResponse({'message': 'Message was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def chat_room(request):
  if request.method == 'GET':
    chats = Chat.objects.all()
    serializer = ChatSerializer(chats, many=True)
    return JsonResponse(serializer.data, safe=False)
  if request.method == 'POST':
    roomName = request.data.get('roomName')
    userName = request.data.get('userName')
    try:
      message = request.data.get('message')
    except:
      message = ""
    chat = Chat.objects.create(roomName=roomName, userName=userName, message=message)
    chat.save()
    return JsonResponse({"status": "201"})

@api_view(['DELETE', 'PUT'])
def chat_edit(request, pk):
  try:
    chat = Chat.objects.get(pk=pk)
  except Chat.DoesNotExist:
    return JsonResponse({'message': 'Message does not exist!'}, status=status.HTTP_204_NO_CONTENT)

  if request.method == 'DELETE':
    chat.delete()
    return JsonResponse({'message': 'Message was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

  if request.method == 'PUT':
    chatData = JSONParser().parse(request)
    serializer = ChatSerializer(chat, data=chatData)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
