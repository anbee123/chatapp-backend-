from rest_framework import serializers

from .models import Message
class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    # fields = '__all__'
    fields = ('id', 'value', 'date', 'user', 'room', 'receiver')
