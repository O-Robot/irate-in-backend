from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from .serializers import ListUserSerializer, CreateUserSerializer


class AuthViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = ListUserSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['email', 'firstname', 'lastname']

    def get_serializer_class(self):
        if self.action in ['create', 'invite_user']:
            return CreateUserSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        permission_classes = self.permission_classes
        if self.action in ['retrieve', 'list', 'create*']:
            permission_classes = [AllowAny]
        elif self.action in ['destroy', 'partial_update']:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]