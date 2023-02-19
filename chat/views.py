from django.http import JsonResponse
from chat.models import Room

def index(request):
    rooms = Room.objects.all()
    data = list(rooms.values())
    return JsonResponse(data, safe=False)