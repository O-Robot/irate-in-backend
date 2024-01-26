from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from decouple import config
from django.contrib.auth import get_user_model
from .utils import send_email
from .user_repository.repository import UserRepository
from .serializers import (ListUserSerializer, CreateUserSerializer,
                          CustomObtainTokenPairSerializer, InviteUserSerializer)


class AuthViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = ListUserSerializer
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['email', 'firstname', 'lastname']

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateUserSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        permission_classes = self.permission_classes
        if self.action in ['retrieve', 'list', 'create']:
            permission_classes = [AllowAny]
        elif self.action in ['destroy', 'partial_update', 'add_user']:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(methods=['POST'], detail=False, url_path='add-user')
    def add_user(self, request, pk=None):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                subject = 'You have been invited to our program'
                email = [request.data['email']]
                user_repository = UserRepository()
                user = user_repository.get_by_email(email)
                client_url = config('CLIENT_URL')
                message = f'You have been invited to our chat app by {request.user.firstname} {request.user.lastname}. Click to join {client_url}/signup'
                send_email(subject, message, email)
                return Response({'success': True}, status=status.HTTP_200_OK)
            return Response({'success': False, 'errors': serializer.errors}, status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class CustomObtainTokenPairView(TokenObtainPairView):
    """Login with email and password"""
    serializer_class = CustomObtainTokenPairSerializer
