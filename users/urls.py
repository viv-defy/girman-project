from django.urls import path

from users.views import add_user, assign_permission, get_users

urlpatterns = [
    path("", add_user, name="create-user"),
    path("list", get_users, name="get-all-users"),
    path("permission", assign_permission, name="assign-user-permission"),
]