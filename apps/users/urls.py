from django.urls import path

from . import views

urlpatterns = [
    path('regitser/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('exit/', views.Exit.as_view()),

    path('users/', views.ListUsers.as_view()),
]