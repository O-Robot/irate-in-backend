from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime
from .managers import CustomUserManager
import uuid

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(null=True, blank=True, unique=True)
    password = models.CharField(max_length=255, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to='users/', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.email

    def save_last_login(self):
        self.last_login = datetime.now()
        self.save()
