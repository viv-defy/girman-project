from django.urls import path

from users.views import add_user, assign_permission, assign_role, get_permissions, get_roles, get_users

urlpatterns = [
    path("", add_user, name="create-user"),
    path("list", get_users, name="get-all-users"),
    path("<int:id>/role", assign_role, name="assign-user-role"),

    path("roles", get_roles, name="get-all-roles"),
    path("roles/<int:id>/permission", assign_permission, name="assign-role-permission"),

    path("permissions", get_permissions, name="get-all-permissions"),
]
