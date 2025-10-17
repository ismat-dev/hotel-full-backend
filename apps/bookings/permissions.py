from rest_framework import permissions

class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "CUSTOMER"
    


class IsReceptionist(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in  ["ADMIN", "RECEPTIONIST", "MANAGER"])
    