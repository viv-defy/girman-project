from django.urls import path

from users.views import add_user, assign_role, get_users

urlpatterns = [
    path("", add_user, name="create-user"),
    path("list", get_users, name="get-all-users"),
    path("<int:id>/role", assign_role, name="assign-user-role"),
]
