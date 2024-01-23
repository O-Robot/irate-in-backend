from rest_framework import serializers
from django.contrib.auth import get_user_model
from email_validator import validate_email, EmailNotValidError

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

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        if validated_data.get('password', False):
            instance.set_password(validated_data.get('password'))
            instance.save()
        return instance
