from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from rest_framework import serializers

from .constants import User


class PasswordSerializer(serializers.ModelSerializer):
    """Password serializer."""

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = User
        fields = ["password"]

    def update(self, user, validated_data):
        """Update user with an encrypted password and return the updated user."""
        password = validated_data.pop("password", None)

        user = super().update(user, validated_data)
        self.set_user_password(password, user)

        return user

    def validate_password(self, password):
        """Validate the password using Django's password validators."""
        django_validate_password(password, self.context["request"].user)
        return password

    def set_user_password(self, password, user: User):
        """Set the encrypted password for the user."""
        if password:
            user.set_password(password)
            user.save()


class UserSerializer(PasswordSerializer):
    """User model serializer. Inherits from PasswordSerializer."""

    class Meta(PasswordSerializer.Meta):
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        ] + PasswordSerializer.Meta.fields

    def create(self, validated_data):
        """Create and return a user with an encrypted password."""
        password = validated_data.pop("password", None)

        user = User.objects.create(**validated_data)
        self.set_user_password(password, user)

        return user
