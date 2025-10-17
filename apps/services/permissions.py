from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "ADMIN"
    
class IsServiceView(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in ["ADMIN", "MANAGER", "RECEPTIONIST", 'CUSTOMER'])
    

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "MANAGER"
    
