from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from users.models import Permission, Role, User
from users.serializers import RoleSerializer, UserSerializer


@api_view(["POST"])
@permission_classes([IsAdminUser])
def add_user(request):
    """
    Add a new user
    """

    username = request.data.get("username", None)
    password = request.data.get("password", None)
    email = request.data.get("email", None)
    if not username or not password or not email:
        return Response(
            {"success": False, "message": "Kindly provide both username, password and email"},
            status=HTTP_400_BAD_REQUEST,
        )

    user = User.objects.create(username=username, password=password, email=email)
    user_serializer = UserSerializer(user)

    return Response(
        {
            "success": True,
            "message": "User data",
            "data": {"user": user_serializer.data},
        },
        status=HTTP_201_CREATED,
    )


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_users(request):
    """
    Get users list
    """

    users = User.objects.all()
    user_serializer = UserSerializer(users, many=True)

    return Response(
        {"success": True, "message": "Users list", "data": user_serializer.data},
        status=HTTP_200_OK,
    )


@api_view(["PATCH"])
@permission_classes([IsAdminUser])
def assign_role(request, id):
    """
    Assign user role
    """

    try:
        user = User.objects.get(id=id)

        role_id = request.data.get("role_id", None)
        if role_id:
            role = Role.objects.get(id=role_id)
            user.add_role(role)

        user_serializer = UserSerializer(user)

        return Response(
            {
                "success": True,
                "message": "Updated user data",
                "data": {"user": user_serializer.data},
            },
            status=HTTP_200_OK,
        )

    except User.DoesNotExist:
        return Response(
            {"success": False, "message": f"The user with id {id} does not exist"},
            status=HTTP_400_BAD_REQUEST,
        )

    except Role.DoesNotExist:
        return Response(
            {"success": False, "message": f"The role with id {role_id} does not exist"},
            status=HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_users(request):
    """
    Get roles list
    """

    roles = Role.objects.all()
    role_serializer = RoleSerializer(roles, many=True)

    return Response(
        {"success": True, "message": "Roles list", "data": role_serializer.data},
        status=HTTP_200_OK,
    )


@api_view(["PATCH"])
@permission_classes([IsAdminUser])
def assign_permission(request, id):
    """
    Assign permissions to roles
    """

    try:
        role = Role.objects.get(id=id)

        permission_id = request.data.get("permission_id", None)
        if permission_id:
            permission = Permission.objects.get(id=permission_id)
            role.add_permission(permission)

        role_serializer = RoleSerializer(role)

        return Response(
            {
                "success": True,
                "message": "Updated role data",
                "data": {"user": role_serializer.data},
            },
            status=HTTP_200_OK,
        )

    except Role.DoesNotExist:
        return Response(
            {"success": False, "message": f"The role with id {id} does not exist"},
            status=HTTP_400_BAD_REQUEST,
        )

    except Permission.DoesNotExist:
        return Response(
            {"success": False, "message": f"The role with id {permission_id} does not exist"},
            status=HTTP_400_BAD_REQUEST,
        )
