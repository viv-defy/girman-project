from django.urls import path

from users.views import (
    add_user,
    api1,
    api2,
    api3,
    api4,
    assign_permission,
    assign_role,
    get_access_logs,
    get_permissions,
    get_role_permissions,
    get_roles,
    get_users,
)

urlpatterns = [
    path("", add_user, name="create-user"),
    path("list", get_users, name="get-all-users"),
    path("<int:id>/role", assign_role, name="assign-user-role"),
    path("roles", get_roles, name="get-all-roles"),
    path("roles/<int:id>/permission", assign_permission, name="assign-role-permission"),
    path("permissions", get_permissions, name="get-all-permissions"),
    path(
        "roles/<int:id>/permissions",
        get_role_permissions,
        name="assign-role-permission",
    ),
    path("api-one", api1, name="api-one"),
    path("api-two", api2, name="api-two"),
    path("api-three", api3, name="api-three"),
    path("api-four", api4, name="api-four"),
    path("access-logs", get_access_logs, name="access-logs"),
]
