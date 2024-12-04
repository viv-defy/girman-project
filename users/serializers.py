from rest_framework import serializers
from users.models import Permission, Role, User


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ["id", "name", "codename", "description"]


class RoleSerializer(serializers.ModelSerializer):

    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Role
        fields = ["id", "name", "permissions"]


class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ["id", "name"]


class UserSerializer(serializers.ModelSerializer):
    """
    List user data
    """

    roles = UserRoleSerializer(many=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_active",
            "date_joined",
            "is_staff",
            "is_superuser",
            "roles",
        ]
