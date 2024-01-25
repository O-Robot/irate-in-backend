from django.contrib.auth import get_user_model
from .models import Chat

def create_chat(user_id1, user_id2, room_name):
    # Get participants
    participants = get_user_model().objects.filter(id__in=[user_id1, user_id2])

    # Get Chat instance
    chat, _ = Chat.objects.get_or_create(name=room_name)

    # Add participants to chat
    chat.participants.add(participants[0])
    chat.participants.add(participants[1])
    chat.save()

    return chat