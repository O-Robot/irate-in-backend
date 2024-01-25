from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

# Create your models here.
class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    # def __str__(self):
    #     return self.author.firstname

class Chat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    participants = models.ManyToManyField(get_user_model(), related_name='chats', blank=True)
    messages = models.ManyToManyField(Message,blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name