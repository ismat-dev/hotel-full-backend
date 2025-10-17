from rest_framework import permissions

class IsStaves(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in ['ADMIN', 'MANAGER', 'RECEPTIONIST', 'ACCOUNTANT'])
    
class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "CUSTOMER"