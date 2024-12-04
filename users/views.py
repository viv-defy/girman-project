from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from users.models import User
from users.serializers import UserSerializer


@api_view(["POST"])
@permission_classes([IsAdminUser])
def add_user(request):
    """
    Add a new user
    """

    username = request.data.get("username", None)
    password = request.data.get("password", None)
    if not username or not password:
        return Response(
            {"success": False, "message": "Kindly provide both username and password"},
            status=HTTP_400_BAD_REQUEST,
        )

    user = User.objects.create(username=username, password=password)
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
def assign_permission(request):
    """
    Assign user permissions
    """

    return Response(
        {"success": True, "message": "Updated user data", "data": {"user": {}}},
        status=HTTP_200_OK,
    )
