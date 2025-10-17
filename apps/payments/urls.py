from django.urls import path

from . import views

urlpatterns = [
    path('payments/', views.all_payments),
    path('payments_create/', views.create_payment),
    path('payments_update/<int:pk>/', views.update_payment),
    path('payments_delete/<int:pk>/', views.delete_payments),
]
