import json
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message, Chat
from .utils import create_chat
from .serializers import MessageSerializer


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        participant1= self.scope['url_route']['kwargs']['participant1_id']
        participant2 = self.scope['url_route']['kwargs']['participant2_id']
        self.room_group_name = 'chat_%s' % self.room_name
        self.chat = create_chat(participant1, participant2, self.room_name)

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        author = get_user_model().objects.get(id=text_data_json['author'])

        # Create new message
        new_message = self.chat.messages.create(content=message, author=author)

        # Serialize message
        serialized_message = MessageSerializer(new_message).data

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'author': str(author.id),
                'created_at': serialized_message['created_at']
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'author': event['author'],
            'createdAt': event['created_at']
        }))
