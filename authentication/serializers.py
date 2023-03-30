from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import User
from django.db.models import Q

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "phone_number"]

class AuthTokenSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def validate(self, attrs):
        email_or_username = attrs.get("email_or_username")
        password = attrs.get("password")

        if email_or_username and password:
            user = (
                User.objects.filter(
                    Q(username=email_or_username) | Q(email=email_or_username)
                )
                .distinct()
                .first()
            )
            if user and user.check_password(password):
                attrs["user"] = user
                return attrs
            else:
                raise serializers.ValidationError(
                    "Unable to log in with provided credentials."
                )
        else:
            raise serializers.ValidationError(
                'Must include "email_or_username" and "password".'
            )


class UserRegiserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    phone_number = serializers.CharField()
    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise ValidationError("this email address is already exist")
        return email
    
    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username

    def validate_password_strong(self, password):
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least 1 digit.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least 1 letter.")
        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least 1 uppercase letter.")
        if not any(char.islower() for char in password):
            raise ValidationError("Password must contain at least 1 lowercase letter.")
        return password

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Those passwords don't match.")
        self.validate_password_strong(password)
        return data