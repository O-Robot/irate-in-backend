from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Chat, Message

from user.serializers import ListUserSerializer

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('__all__')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        users = get_user_model().objects.filter(id__in=representation['participants'])
        messages = Message.objects.filter(id__in=representation['messages']).order_by('created_at')
        representation['participants'] = ListUserSerializer(users, many=True).data
        representation['messages'] = MessageSerializer(messages, many=True).data
        return representation

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('__all__')