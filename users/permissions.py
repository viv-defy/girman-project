from rest_framework.permissions import BasePermission

class L1Permission(BasePermission):

    def has_permission(self, request, view):

        return request.user.is_superuser or request.user.has_permission("level1")
    

class L2Permission(BasePermission):

    def has_permission(self, request, view):
        
        return request.user.is_superuser or request.user.has_permission("level2")

    

class L3Permission(BasePermission):

    def has_permission(self, request, view):

        return request.user.is_superuser or request.user.has_permission("level3")
