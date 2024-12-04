from rest_framework import serializers
from users.models import Role, User


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ["id", "name"]


class UserSerializer(serializers.ModelSerializer):
    """
    List user data
    """

    roles = RoleSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "is_active", "created_at", "updated_at", "roles"]
