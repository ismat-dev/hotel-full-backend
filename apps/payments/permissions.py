from rest_framework import permissions

class IsPaymentOccur(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in ["ADMIN", "RECEPTIONIST", "CUSTOMER"])
    
class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "CUSTOMER"