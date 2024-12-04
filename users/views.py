from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED


@api_view(["POST"])
@permission_classes([IsAdminUser])
def add_user(request):
    """
    Add a new user
    """

    return Response(
        {
            "success": True,
            "message": "User data",
            "data": {"user": {}}
        },
        status=HTTP_201_CREATED
    )


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_users(request):
    """
    Get a list of users
    """

    return Response(
        {
            "success": True,
            "message": "Users list",
            "data": {}
        },
        status=HTTP_200_OK
    )


@api_view(["PATCH"])
@permission_classes([IsAdminUser])
def assign_permission(request):
    """
    Assign user permissions
    """

    return Response(
        {
            "success": True,
            "message": "Updated user data",
            "data": {"user": {}}
        },
        status=HTTP_200_OK
    )
    