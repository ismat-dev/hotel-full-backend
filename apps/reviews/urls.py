from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.CommentList.as_view()),
    path('reviews_create/', views.CommentCreate.as_view()),
    path('reviews_update_delete_by_admin/<int:pk>/', views.AdminRetrieveUpdateDestroyAPIView.as_view()),
    path('reviews_update_delete_by_customer/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),
]
