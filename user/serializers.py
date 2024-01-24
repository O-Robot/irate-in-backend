from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from email_validator import validate_email, EmailNotValidError
from .user_repository.repository import UserRepository

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'firstname', 'lastname',
                  'email', 'image', 'last_login', 'created_at']


class CreateUserSerializer(serializers.ModelSerializer):
    """Serializer for user object"""

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'firstname',
                  'lastname', 'image', 'created_at')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8},
                        'last_login': {'read_only': True}}

    def validate(self, attrs):
        email = attrs.get('email', None)
        if email:
            email = attrs['email'].lower().strip()
            try:
                valid = validate_email(attrs['email'])
                attrs['email'] = valid.email
                return super().validate(attrs)
            except EmailNotValidError as e:
                raise serializers.ValidationError(e)
        return super().validate(attrs)

    def create(self, validated_data):
        user_repository = UserRepository()
        user = user_repository.create(validated_data)
        return user

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if validated_data.get('password', False):
            instance.set_password(validated_data.get('password'))
            instance.save()
        return instance


class CustomObtainTokenPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        if not user.is_active:
            raise exceptions.AuthenticationFailed(
                _('Account not yet active.'), code='authentication')
        token = super().get_token(user)
        # Add custom claims
        token.id = user.id
        token['email'] = user.email
        if user.firstname and user.lastname:
            token['fullname'] = user.firstname + ' ' + user.lastname
        if user.image:
            token['image'] = user.image.url
        user.save_last_login()
        return token