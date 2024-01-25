from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Chat
from .serializers import ChatSerializer


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', ]

    def get_queryset(self):
        return self.request.user.chats.all()
