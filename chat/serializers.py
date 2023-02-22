from rest_framework import serializers

from .models import Message
# from .models import User
class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    # fields = '__all__'
    fields = ('id', 'value', 'date', 'user', 'room', 'receiver')

# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = User
#     fields = ('id', 'name', 'email', 'password')
