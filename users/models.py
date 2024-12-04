from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField("Permission", related_name='roles', blank=True)

    def __str__(self):
        return self.name
    
    def add_permission(self, permission):
        """
        Assign a permission to the user.
        """
        self.permissions.add(permission)
    
    class Meta:
        db_table = "role"


class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    codename = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.codename
    
    class Meta:
        db_table = "permission"


class User(AbstractUser):
    """
    User model, inherited from Django Abstract User
    """

    first_name = None
    last_name = None
    last_login = None

    roles = models.ManyToManyField(Role, related_name="users", blank=True)
    permissions = models.ManyToManyField("Permission", related_name="users", blank=True)

    def __str__(self):
        return self.username

    def has_permission(self, codename):
        """
        Check if the user has a specific permission.
        """
        return (
            self.permissions.filter(codename=codename).exists()
            or self.roles.filter(permissions__codename=codename).exists()
        )

    def add_role(self, role):
        """
        Assign a role to the user.
        """
        self.roles.add(role)

    def remove_role(self, role):
        """
        Remove a role from the user.
        """
        self.roles.remove(role)

    def add_permission(self, permission):
        """
        Assign a permission to the user.
        """
        self.permissions.add(permission)

    def remove_permission(self, permission):
        """
        Remove a permission from the user.
        """
        self.permissions.remove(permission)

    class Meta:
        db_table = "user"
