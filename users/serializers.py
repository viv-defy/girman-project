from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    List users
    """

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "is_active",
            "created_at",
            "updated_at",
        ]