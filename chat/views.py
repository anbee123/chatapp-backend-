from django.shortcuts import render
# from django.http import HttpResponse
from django.http.response import JsonResponse
# from .models import Message
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
from chat.models import Message
from chat.serializers import MessageSerializer
from rest_framework.decorators import api_view

def index(request):
  return HttpResponse('<h1> MY INDEX PAGE </h1>')

@api_view(['GET', 'POST'])
def chat_list(request):
  if (request.method == 'GET'):
    messages = Message.objects.all()
    messages_serializer = MessageSerializer(messages, many=True)
    return JsonResponse(messages_serializer.data, safe=False)
  elif request.method == 'POST':
    chat_data = JSONParser


# class Message(APIView):

#   def get(self, request):
#     # Index Request
#     print(request)
#     # Get all messages from the chat table
#     messages = Message.objects.all()
#     # Use serializer to format table data to JSON
#     data = MessageSerializer(messages, many=True).data
#     return Response(data)
  
#   def post(self, request):
#     # Post Request
#     print(request.data)
#     # format data for postgres
#     chat = MessageSerializer(data=request.data)
#     if chat.is_valid():
#       chat.save()
#       return Response(chat.data, status=status.HTTP_201_CREATED)
#     else: 
#       return Response(chat.errors, status=status.HTTP_400_BAD_REQUEST)
    
