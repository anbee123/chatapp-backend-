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
from rest_framework.parsers import JSONParser
from rest_framework import status

def index(request):
  return HttpResponse('<h1> MY INDEX PAGE </h1>')

@api_view(['GET', 'POST', 'DELETE'])
def chat_list(request):
  if (request.method == 'GET'):
    messages = Message.objects.all()
    messages_serializer = MessageSerializer(messages, many=True)
    return JsonResponse(messages_serializer.data, safe=False)
  elif request.method == 'POST':
    chat_data = JSONParser().parse(request)
    chat_serializer = MessageSerializer(data=chat_data)
    if chat_serializer.is_valid():
      chat_serializer.save()
      return JsonResponse(chat_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(chat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    count = Message.objects.all().DELETE()
    return JsonResponse({'message': '{} Messages were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def chat_detail(request, pk):
  try:
    chat = Message.objects.get(pk=pk)
  except Message.DoesNotExist:
    return JsonResponse({'message': 'The messages does not exist'},
    status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'GET':
    chat_serializer = MessageSerializer(chat)
    return JsonResponse(chat_serializer.data)

  elif request.method == 'PUT':
    chat_data = JSONParser().parse(request)
    chat_serializer = MessageSerializer(chat, data=chat_data)
    if chat_serializer.is_valid():
      chat_serializer.save()
      return JsonResponse(chat_serializer.data)
    return JsonResponse(chat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    chat.delete()
    return JsonResponse({'message': 'Message was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



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
    
